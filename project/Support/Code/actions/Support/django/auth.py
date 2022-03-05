from accounts.models import User
from ..forms.for_fields import set_slug
from django.contrib import auth
from django.utils.text import slugify
from ..utils.main import gets
from Support.Code.actions._accounts.login_group.login import get_aleatory_profile_photo, construct_user_my_static_page
from Support.Code.actions.Support.utils.functions_dict import get_name

def validate_login(request, process: dict):
    user_type, password = gets(request.POST, process['type'], 'password')
    filter_obj = {process['type']: user_type}
    
    user_for_login = User.objects.filter(**filter_obj).first()
    
    if user_for_login is None:
        return  {'status': 'invalid', 'errors': {process['type']: process['error_message']}}

    user = auth.authenticate(request, username=user_for_login.username, password=password)
    
    if user is not None:
        return {'status': 'valid', 'errors': {}, 'user': user}
    else:
        return {'status': 'invalid', 'errors': {'password': 'Senha incorreta'}}

def login(request, user):
    auth.login(request, user)

    
    
    
def create_user_with_email(fields: dict):
    new_user = User(
        username=fields['email'], name=get_name(fields['name']),
        email=fields['email'], slug=slugify(fields['name']),
        photo=get_aleatory_profile_photo(), 
    )
    new_user.my_static_pages = construct_user_my_static_page(new_user)
    new_user.set_password(fields['password'])
    new_user.save()
    
    
    
def check_password(request, current_password):
    current_password_value = request.POST.get(current_password)
    user = auth.authenticate(request, username=request.user.username, password=current_password_value)
    if user is not None:
        return {'status': 'valid', 'errors': {}}
    else:
        return {'status': 'invalid', 'errors': { current_password: 'Senha incorreta' }}


def change_password(request, new_password: str):
    new_password_value = request.POST.get(new_password)
    user = request.user
    user.set_password(new_password_value)
    user.save()

def anonymous_change_password(email, new_password_value: str):
    user = User.objects.get(email=email)
    user.set_password(new_password_value)
    user.save()


def logout(request):
    auth.logout(request)
    

def create_login_save(request, user):
    request.session['user_save'] = user.my_static_pages