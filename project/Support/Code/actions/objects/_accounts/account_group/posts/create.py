create_post_form_1 = {

    'fields': [
        {'name': 'title', 'label': 'Título', 'placeholder': 'Adicionar título', 'block': 'input'},
        {'name': 'img', 'block': 'img', 'src': '/media/assets/posts/post/nulli.png'},
        {'name': 'description', 'label': 'Descrição', 'placeholder': 'Adicionar descrição', 'block': 'input'},
    ],

    'blocks': {

        'input': {

            'html_structure': """
            <div class="ag-form-group">
                <label for="[name]" class="ag-label">[label]</label>
                <input type="text" name="[name]" id="id_[name]" class="input" placeholder="[placeholder]">
                <div class="error"></div>
            </div>
            """,
            'changes': [
                ('[name]', 'name'), ('[placeholder]', 'placeholder'), 
                ('[label]', 'label'),
            ],
            'validation_type': 'input',
            'history': 'name',
            
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
            'history': 'name',
        },

    }
    
}

def load_data(categories: list, subcategories: list, current_post_form: dict):
    category_html = ''
    subcategory_html = ''
    for category in categories:
        category_html += f'<option value="{category.name}">{category.name}</option>'
    for subcategory in subcategories:
        subcategory_html += f'<div class="ag-check-box cb-category" for="{subcategory.category.name}"><span><input type="checkbox" name="subcategory" id="id_subcategory" value="checked"><span class="checkbox-label">{subcategory.name}</span></span></div>'
    current_post_form['fields'][0] = {**current_post_form['fields'][0], 'categories': category_html}
    current_post_form['fields'][1] = {**current_post_form['fields'][1], 'subcategories': subcategory_html}


create_post_form_2 = {

    'fields': [
        {'name': 'categories', 'block': 'category_list'},
        {'name': 'subcategories', 'block': 'subcategory_list'},
    ],

    'blocks': {

        'category_list': {

            'html_structure': """
                <div class="ag-form-group">
                    <label for="id_category" class="ag-label">Categoria:</label>
                    <select name="category" id="id_category" class="ag-select">
                        [categories]
                    </select>
                    <div class="error"></div>
                </div>
            """,
            'changes': [
                ('[categories]', 'categories')
            ],
            'validation_type': 'select',
            'history': 'name',
            
        },

        'subcategory_list': {

            'html_structure': """
        <div class="ag-form-group">
            <label for="id_subcategory" class="ag-label">Subcategorias:</label>
                [subcategories]
                <div class="error"></div>

        </div>
            """,
            'changes': [
                ('[subcategories]', 'subcategories'), 
            ],
            'validation_type': 'checkbox',
            'history': 'name',
        },

    }
    
}


