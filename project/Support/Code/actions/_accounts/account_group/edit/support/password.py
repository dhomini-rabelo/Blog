from Support.Code.actions.Support.forms.form import Form


def construct_form():
    password_form = Form()
    
    fields = [
        {'name': 'current_password', 'label': 'Senha atual:', 'placeholder': 'Digite sua senha atual'},
        {'name': 'new_password', 'label': 'Nova senha:', 'placeholder': 'Digite sua nova senha'},
        {'name': 'confirm_new_password', 'label': 'Confirmar senha:', 'placeholder': 'Confirme sua nova senha'},
    ]

    html_structure = """
    <div class="ag-form-group">
        <label for="name" class="ag-label">[label]</label>
        <input type="password" name="[name]" id="id_[name]" class="input" placeholder="[placeholder]">
    </div>
    """
 
    password_form.add_fields(fields, html_structure, [
        ('[name]', 'name'), ('[label]', 'label'), ('[placeholder]', 'placeholder'), 
    ])

    return password_form 


def load_form(request):
    password_form = Form()

    if request.session.get('password_fields') is None:
        password_form.load_form(request.session['password_form'])
    else:
        password_form.load_form_with_values(request.session['password_form'], request.session['password_fields'])
        request.session['password_form'] = None
        request.session['password_fields'] = None
       
    return password_form


def save_form(request, form_class):
    request.session['password_form'] = form_class.form_for_save()