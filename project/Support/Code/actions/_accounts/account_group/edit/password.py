from Support.Code.actions.Support.forms.form import validate_form
from Support.Code.actions.Support.django.messages import success_message, error_message
from .support.password import construct_form, load_form, save_form, check_for_message
from accounts.models import User
from django.contrib import auth


def get_password_form(request):
    if request.session.get('password_form') is None:
        form = construct_form()
        save_form(request, form)
    else:
        form = load_form(request)

    return form.get_form()