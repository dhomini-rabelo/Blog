from Support.Code.actions.Support.form import Form


def construct_form():
    login_form = Form()
    
    fields = [
        {'name': 'email', 'label': 'Email', 'placeholder': 'Digite seu email', 'type': 'text', 'forgot': ''},
        {'name': 'password', 'label': 'Senha', 'placeholder': 'Digite sua senha', 'type': 'password', 'forgot': '<div class="block-forgot-password"><a href="">Esqueceu a senha?</a></div>'},
    ]

    html_structure = """
    <div class="field-group">
        <label for="id_[name]">[label]:</label>
        <input type="[type]" name="[name]" id="id_[name]" placeholder="[placeholder]">
        [forgot]
        <div class="error"></div>
    </div>
    """
 
    login_form.add_fields(fields, html_structure, [('[name]', 'name'), ('[label]', 'label'), ('[placeholder]', 'placeholder'), ('[type]', 'type'), ('[forgot]', 'forgot')])

    return login_form


def load_form(request):
    login_form = Form()
    login_form.load_form(request.session['login_form'])
    
    return login_form

def save_form(request, form_class):
    request.session['login_form'] = form_class.form_for_save()