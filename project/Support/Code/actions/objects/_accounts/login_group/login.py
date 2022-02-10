login_form = {
    
    'fields' : [
        {'name': 'email', 'label': 'Email', 'placeholder': 'Digite seu email', 'type': 'text', 'forgot': ''},
        {'name': 'password', 'label': 'Senha', 'placeholder': 'Digite sua senha', 'type': 'password', 'forgot': '<div class="block-forgot-password"><a href="">Esqueceu a senha?</a></div>'},
    ],

    'html_structure' : """
    <div class="field-group">
        <label for="id_[name]">[label]:</label>
        <input type="[type]" name="[name]" id="id_[name]" placeholder="[placeholder]">
        [forgot]
        <div class="error"></div>
    </div>
    """,
    
    'changes': [
        ('[name]', 'name'), ('[label]', 'label'), ('[placeholder]', 'placeholder'), 
        ('[type]', 'type'), ('[forgot]', 'forgot'),
    ]
    
}


login_form_validation = {

    'form_base': {
        'fields': [
            ['email', []], ['password', []],
        ]
    },

}


login_obj = {
    
    'type': 'email',
    'error_message': 'Email não encontrado'
    
}