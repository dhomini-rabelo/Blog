from accounts.models import User


password_form = {
    
    'fields' : [
        {'name': 'current_password', 'label': 'Senha atual:', 'placeholder': 'Digite sua senha atual'},
        {'name': 'new_password', 'label': 'Nova senha:', 'placeholder': 'Digite sua nova senha'},
        {'name': 'confirm_new_password', 'label': 'Confirmar senha:', 'placeholder': 'Corfirme sua nova senha'},

    ],

    'html_structure' : """
    <div class="ag-form-group">
        <label for="[name]" class="ag-label">[label]</label>
        <input type="password" name="[name]" id="id_[name]" class="input" placeholder="[placeholder]">
        <div class="error"></div>
    </div>
    """,
    
}

password_form_validation = {
    
    'form_base': {
        'fields': [
            ['current_password', []],
            ['new_password', [('min_length', 8), ('max_length', 256)]], 
            ['confirm_new_password'],
        ]
    },
    
    'equal_fields': [
        ['new_password', 'confirm_new_password', 'As senhas são diferentes'],
    ],
    
    'keys_order': [
        'equal_fields',    
    ],  
    
}


password_message = {
    
    'title': 'success_change_password',
    'message': 'Senha alterada',
    'type': 'success'
    
}


