from Support.Code.actions.Support.form import Form
from .support.login import construct_form, load_form, save_form

def get_login_form(request):
    if request.session.get('login_form') is None:
        form = construct_form()
        save_form(request, form)
    else:
        form = load_form(request)

    return form.get_form()
