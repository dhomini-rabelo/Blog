from accounts.models import User


new_email_form = {
    
    'fields' : [
        {'name': 'new_email', 'label': 'Novo email:', 'placeholder': 'Digite seu novo email'},
        {'name': 'confirm_new_email', 'label': 'Confirmar email:', 'placeholder': 'Corfirme seu novo email'},
    ],

    'html_structure' : """
    <div class="ag-form-group">
        <label for="[name]" class="ag-label">[label]</label>
        <input type="text" name="[name]" id="id_[name]" class="input" placeholder="[placeholder]">
        <div class="error"></div>
    </div>
    """,
    
}

new_email_form_validation = {
    
    'form_base': {
        'fields': [
            ['new_email',  [('max_length', 128), ('email',), ('unique', User, 'email')]], 
            ['confirm_new_email'],
        ]
    },
    
    'equal_fields': [
        ['new_email', 'confirm_new_email', 'Os emails são diferentes'],
    ],
    
    'adapt_message_errors': {
        'email': [
            ['Este campo já está em uso', 'Email já foi cadastrado']
        ]
    },
    
    'keys_order': [
        'equal_fields',    
    ],  
    
}