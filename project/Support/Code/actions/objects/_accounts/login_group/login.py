from accounts.models import User


login_form = {
    
    'fields' : [
        {'name': 'email', 'label': 'Email', 'placeholder': 'Digite seu email', 'type': 'text', 'forgot': '', 'input_mode': ' inputmode="email"'},
        {'name': 'password', 'label': 'Senha', 'placeholder': 'Digite sua senha', 'type': 'password', 'forgot': '<div class="block-forgot-password"><a href="/nova-senha/informar-email">Esqueceu a senha?</a></div>', 'input_mode': ''},
    ],

    'html_structure' : """
    <div class="field-group">
        <label for="id_[name]">[label]:</label>
        <input type="[type]" name="[name]" id="id_[name]" placeholder="[placeholder]"[input_mode]>
        [forgot]
        <div class="error"></div>
    </div>
    """,
    
    'changes': [
        ('[name]', 'name'), ('[label]', 'label'), ('[placeholder]', 'placeholder'), 
        ('[type]', 'type'), ('[forgot]', 'forgot'),
    ]
    
}

forgot_password_email_form = {
    
    'fields': [
        {'name': 'email', 'label': 'Email'} 
    ],
    
    'html_structure': """
    <div class="field-group">
        <label for="id_[name]">[label]:</label>
        <input type="text" name="[name]" id="id_[name]" placeholder="Digite seu email">
        <div class="error"></div>
    </div>
    """,
    
    'changes': [('[name]', 'name'), ('[label]', 'label')],

}


forgot_password_form = {
    
    'fields': [
        {'name': 'new_password', 'label': 'Nova senha', 'placeholder': 'Digite sua nova senha'},
        {'name': 'confirm_new_password', 'label': 'Confirmar senha', 'placeholder': 'Corfirme sua nova senha'},
    ],
    
    'html_structure': """
    <div class="field-group">
        <label for="id_[name]">[label]:</label>
        <input type="text" name="[name]" id="id_[name]" placeholder="[placeholder]">
        <div class="error"></div>
    </div>
    """,
    
}


login_form_validation = {

    'form_base': {
        'fields': [
            ['email', []], ['password', []],
        ]
    },

}

forgot_password_email_form_validation = {

    'form_base': {
        'fields': [
            ['email', [('exists', User, 'email')]],
        ]
    },

    'adapt_message_errors': {
        'email': [
            ['Este campo não foi cadastrado', 'Email não cadastrado']
        ]
    },

}

forgot_password_form_validation = {

    'form_base': {
        'fields': [
            ['new_password', [('min_length', 8), ('max_length', 256)]], 
            ['confirm_new_password'],
        ]
    },

    'equal_fields': [
        ['new_password', 'new_confirm_password', 'As senhas são diferentes']
    ],

    'keys_order': [
        'equal_fields',    
    ],  

}


login_obj = {
    
    'type': 'email',
    'error_message': 'Email não encontrado'
    
}

user_save = {
    'photo_path': lambda user: user.photo.url,
    'name': 'name',
    'email': 'email'
}