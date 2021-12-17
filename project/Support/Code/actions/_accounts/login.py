from Support.Code.actions.Support.form import validate_form
from Support.Code.actions.Support.messages import success_message, error_message
from .support.login import construct_form, load_form, save_form, check_for_message
from accounts.models import User
from django.contrib import auth


def get_login_form(request):
    if request.session.get('login_form') is None:
        form = construct_form()
        save_form(request, form)
    else:
        form = load_form(request)

    return form.get_form()





def load_messages_in_login_page(request):
    messages = []
    success_checks = [('show_success_message_for_user_register', 'Usuário criado com sucesso')]
    error_checks = []

    for check, message in success_checks:
        check = check_for_message(request, check)
        if check:
            messages.append(success_message(message))

    for check, message in error_checks:
        check = check_for_message(request, check)
        if check:
            messages.append(error_message(message))
      
    return messages


def validate_login_form(request):
    form_validation = [
        ['email', []], ['password', []],
    ]

    validation = validate_form(request.POST, *form_validation)

    return validation


def login(request):
    rp = request.POST
    email, password = rp.get('email'), rp.get('password')

    user_for_login = User.objects.filter(email=email).first()

    if user_for_login is None:
        return {'status': 'invalid', 'errors': {'email': 'Email não encontrado'}}


    user = auth.authenticate(request, username=user_for_login.username, password=password)

    if user is not None:
        auth.login(request, user)
        return {'status': 'valid', 'errors': {}}
    else:
        return {'status': 'invalid', 'errors': {'password': 'Senha incorreta'}}


        
 


def save_login_form_errors(request, errors: dict):
    form = construct_form()
    form.show_errors(errors)

    request.session['login_form'] = form.form_for_save()


def save_login_form_fields_values(request, fields: dict):
    request.session['login_fields'] = fields


def save_server_error_of_login_process(request):
    request.session['server_error_of_login_process'] = True