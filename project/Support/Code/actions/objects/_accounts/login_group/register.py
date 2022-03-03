from accounts.models import User


register_form = {
    
    'fields' : [
        {'name': 'name', 'label': 'Nome', 'placeholder': 'Digite seu nome', 'type': 'text', 'input_mode': ''},
        {'name': 'email', 'label': 'Email', 'placeholder': 'Digite seu email', 'type': 'text', 'input_mode': ' inputmode="email"'},
        {'name': 'password', 'label': 'Senha', 'placeholder': 'Digite sua senha', 'type': 'password', 'input_mode': ''},
        {'name': 'confirm_password', 'label': 'Confirmar senha', 'placeholder': 'Confirme sua senha', 'type': 'password', 'input_mode': ''},
    ],
    
    'html_structure': """
        <div class="field-group">
            <label for="id_[name]">[label]:</label>
            <input type="[type]" name="[name]" id="id_[name]" placeholder="[placeholder]"[input_mode]>
            <div class="error"></div>
        </div>
    """,
    
    'changes' : [
        ('[name]', 'name'), ('[label]', 'label'), ('[placeholder]', 'placeholder'), 
        ('[type]', 'type'), ('[input_mode]', 'input_mode')
    ]
    
}


register_email_confirmation_form = {
    
    'fields': [
        {'name': 'code', 'label': 'Código de verificação'} 
    ],
    
    'html_structure': """
    <div class="field-group">
        <label for="id_[name]">[label]:</label>
        <input type="text" name="[name]" id="id_[name]" placeholder="Digite o código" inputmode="numeric">
        <div class="error"></div>
    </div>
    """,
    
    'changes': [('[name]', 'name'), ('[label]', 'label')]
    
}


register_form_validation = {

    'form_base': {
        'fields': [
            ['name', [('only_str',), ('max_length', 256)]], 
            ['email', [('max_length', 128), ('email',), ('unique', User, 'email')]], 
            ['password', [('min_length', 8), ('max_length', 256)]], 
            ['confirm_password'],
        ]
    },
    
    'equal_fields': [
        ['password', 'confirm_password', 'As senhas são diferentes']
    ],
    
    'adapt_message_errors': {
        'email': [
            ['Este campo já está em uso', 'Email já está em uso']
        ]
    },
    
    'keys_order': [
        'equal_fields',    
    ],  

}



register_save_message = {
    
    'title': 'success_register',
    'message': 'Usuário criado com sucesso',
    'type': 'success'
     
}