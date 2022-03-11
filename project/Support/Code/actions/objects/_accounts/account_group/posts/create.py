create_post_form = {

    'fields': [
        {'name': 'title', 'label': 'Título', 'placeholder': 'Adicionar título', 'block': 'input'},
        {'name': 'img', 'block': 'img'},
        {'name': 'description', 'label': 'Descrição', 'placeholder': 'Adicionar descrição', 'block': 'input'},
    ],

    'blocks': {

        'input': {

            'html_structure': """
            <div class="ag-form-group">
                <label for="[name]" class="ag-label">[label]</label>
                <input type="text" name="[name]" id="id_[name]" class="input" placeholder="[placeholder]" value="[value]">
                <div class="error"></div>
            </div>
            """,
            'changes': [
                ('[name]', 'name'), ('[placeholder]', 'placeholder'), 
                ('[label]', 'label'), ('[value]', 'value'),
            ],
            'validation_type': 'input',
            'history': 'value',
            
        },

        'img': {

            'html_structure': """
            <div class="ag-form-group">
                <label for="img" class="ag-label">Imagem:</label>
                <span class="ag-help-title">clique para alterar</span>
                <div class="img-container">
                    <img src="[src]" alt="post-img" id="post-img">
                    <input type="file" name="img" id="id_img" accept="image/*">
                </div>
                <div class="error"></div>
            </div>
            """,
            'changes': [
                ('[src]', 'src'), 
            ],
            'validation_type': 'img',
            'history': 'src',
        },

    }
    
}