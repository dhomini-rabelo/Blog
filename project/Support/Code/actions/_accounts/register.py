from .support.register import construct_form, load_form, save_form


def get_register_form(request):
    if request.session.get('register_form') is None:
        form = construct_form()
        save_form(request, form)
    else:
        form = load_form(request)

    return form.get_form()



def validate_user_form(request):
    pass


