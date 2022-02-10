from accounts.models import User
from ..forms.for_fields import set_slug
from django.contrib import auth
from ..utils.main import gets




def login(request, process: dict):
    user_type, password = gets(request.POST, process['type'], 'password')
    filter_obj = {process['type']: user_type}
    
    user_for_login = User.objects.filter(**filter_obj).first()
    
    if user_for_login is None:
        return  {'status': 'invalid', 'errors': {process['type']: process['error_message']}}

    user = auth.authenticate(request, username=user_for_login.username, password=password)

    if user is not None:
        auth.login(request, user)
        return {'status': 'valid', 'errors': {}}
    else:
        return {'status': 'invalid', 'errors': {'password': 'Senha incorreta'}}
    
    
    
def create_user_with_email(fields: dict):
    new_user = User(
        username=fields['email'], name=fields['name'].title(),
        email=fields['email'], slug=set_slug(fields['name'])
    )
    new_user.set_password(fields['password'])
    new_user.save()
    
    

def change_password(request, current_password: str, new_password: str):
    current_password_value, new_password_value = gets(request.POST, current_password, new_password)
    
    user = auth.authenticate(request, username=request.user.username, password=current_password_value)
    
    if user is not None:
        user.set_password(new_password_value)
        user.save()
        return {'status': 'valid', 'errors': {}}
    return {'status': 'invalid', 'errors': { current_password: 'Senha incorreta' }}



def logout(request):
    auth.logout(request)
    
