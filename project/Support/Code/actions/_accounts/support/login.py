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

    if request.session.get('login_fields') is None:
        login_form.load_form(request.session['login_form'])
    else:
        login_form.load_form_with_values(request.session['login_form'], request.session['login_fields'])
        request.session['login_form'] = None
        request.session['login_fields'] = None
       
    return login_form

def save_form(request, form_class):
    request.session['login_form'] = form_class.form_for_save()
    

def check_for_message(request, check):
    show = request.session.get(check)
    if show:
        request.session[check] = False
    
    return show if show is not None else False

