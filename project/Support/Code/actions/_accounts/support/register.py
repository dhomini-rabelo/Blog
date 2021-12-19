from Support.Code.actions.Support.form import Form

def construct_form():
    register_form = Form()
    
    fields = [
        {'name': 'name', 'label': 'Nome', 'placeholder': 'Digite seu nome', 'type': 'text'},
        {'name': 'email', 'label': 'Email', 'placeholder': 'Digite seu email', 'type': 'text'},
        {'name': 'password', 'label': 'Senha', 'placeholder': 'Digite sua senha', 'type': 'password'},
        {'name': 'confirm_password', 'label': 'Confirmar senha', 'placeholder': 'Confirme sua senha', 'type': 'password'},
    ]

    html_structure = """
    <div class="field-group">
        <label for="id_[name]">[label]:</label>
        <input type="[type]" name="[name]" id="id_[name]" placeholder="[placeholder]">
        <div class="error"></div>
    </div>
    """

    register_form.add_fields(fields, html_structure, [('[name]', 'name'), ('[label]', 'label'), ('[placeholder]', 'placeholder'), ('[type]', 'type')])

    return register_form


def load_form(request):
    register_form = Form()

    if request.session.get('register_fields') is None:
        register_form.load_form(request.session['register_form'])
    else:
        register_form.load_form_with_values(request.session['register_form'], request.session['register_fields'])
        request.session['register_form'] = None
        request.session['register_fields'] = None

    return register_form


def save_form(request, form_class):
    request.session['register_form'] = form_class.form_for_save()
    