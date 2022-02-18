basic_form = {
    
    'fields' : [
        {'name': 'photo', 'src': '', 'block': 'imgFile'},
        {'name': 'name', 'value': '', 'block': 'input'},
    ],

    'blocks': {
        
        'imgFile': {

            'html_structure': """
            <div class="ag-form-group">
                <label for="name" class="ag-label">Perfil:</label>
                <div class="profile-photo center-c">
                    <span class="help-ag-edit-basic">clique para alterar</span>
                    <img src="[user_path]" alt="profile-photo-img" class="account-img" id="id_profile_img">
                </div>
                <input type="file" accept="image/*" name="photo" id="id_photo">
                <div class="error"></div>
            </div>
            """,
            'changes': [
                ('[user_path]', 'src'), 
            ],
            'validation_type': 'img',
            'history': 'src',

        },
        
        'input': {
            
            'html_structure': """
            <div class="ag-form-group">
                <label for="name" class="ag-label">Nome:</label>
                <input type="text" name="name" id="id_name" class="input" placeholder="Alterar nome" value="[value]">
                <div class="error"></div>
            </div>
            """,
            'changes': [
                ('[value]', 'value'), 
            ],
            'validation_type': 'input',
            'history': 'value',

        },
        
    }
    
}


basic_form_validation = {
    
    'form_base': {
        'fields': [
            ['name', [('only_str',), ('max_length', 256)]], 
        ]
    },
    
}


basic_form_message = {
    
    'title': 'success_basic_form',
    'message': 'Usuário alterado com sucesso',
    'type': 'success'
    
}