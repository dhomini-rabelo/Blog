from Support.Code.actions.Support.form import Form

def get_register_form_class():
    register_form = Form()
    
    fields = [
        {'name': 'name', 'label': 'Nome'},
        {'name': 'email', 'label': 'Email'},
        {'name': 'password', 'label': 'Senha'},
        {'name': 'confirm_password', 'label': 'Confirmar senha'},
    ]

    html_structure = """
    <div class="field-group">
        <label for="id_[name]">[label]:</label>
        <input type="text" name="[name]" id="id_[name]" placeholder="Digite seu nome">
        <div class="error"></div>
    </div>
    """

    register_form.add_charfields(fields, html_structure)

    return register_form
