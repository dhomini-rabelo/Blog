from django.http import request
from accounts.models import User
from .support.register import construct_form, load_form, save_form
from Support.Code.actions.Support.form import Form, validate_form
from Support.Code.actions.Support.for_fields import set_slug





def get_register_form(request):
    if request.session.get('register_form') is None:
        form = construct_form()
        save_form(request, form)
    else:
        form = load_form(request)

    return form.get_form()



def validate_register_form(request):
    form_validation = [
        'name', ['email', [('max_length', 128), ('email',), ('unique', User, 'email')]], 
        ['password', [('min_length', 8), ('max_length', 256)]], 'confirm_password'
    ]

    validation = validate_form(request.POST, *form_validation)

    if (validation['errors'].get('confirm_password') is None) and (request.POST.get('confirm_password') != request.POST.get('password')):
        validation['status'] = 'invalid'
        validation['errors'].update({'confirm_password': 'As senhas são diferentes'})

    if validation['errors'].get('email') == 'Este campo já está em uso':
        validation['errors']['email'] = 'Email já está em uso'

    

    return validation


def save_register_form_errors(request, errors: dict):
    form = construct_form()
    form.show_errors(errors)
    
    request.session['register_form'] = form.form_for_save()


def create_user(fields: dict):
    User.objects.create(
        username=fields['email'], name=fields['name'],
        email=fields['email'], password=fields['password'],
        slug=set_slug(fields['name'])
    )
    

def save_register_form_fields_values(request, fields: dict):
    request.session['register_fields'] = fields


def delete_register_form_fields_values(request):
    request.session['register_fields'] = None


def show_success_message_for_user_register(request):
    request.session['show_success_message_for_user_register'] = True

