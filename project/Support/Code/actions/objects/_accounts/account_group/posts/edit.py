def load_edit_post_1_data(current_post_form: dict, post):
    current_post_form['fields'][0]['value'] = post.title
    current_post_form['fields'][2]['value'] = post.description
    current_post_form['fields'][1]['src'] = post.img.url


edit_post_form_1 = {

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


def load_edit_post_2_data(categories: list, subcategories: list, current_post_form: dict, post):
    category_html = ''
    subcategory_html = ''
    for category in categories:
        if category['slug'] == post.category.slug:
            category_html += f'<option value="{category["slug"]}" selected>{category["name"]}</option>'
        else:
            category_html += f'<option value="{category["slug"]}">{category["name"]}</option>'
    for subcategory in subcategories:
        if subcategory['slug'] in post.sub_categories.values_list('slug', flat=True):
            subcategory_html += f'<div class="ag-check-box cb-category" for="{subcategory["category"]}"><span><input type="checkbox" name="subcategory" id="id_subcategory" value="{subcategory["slug"]}" checked><span class="checkbox-label">{subcategory["name"]}</span></span></div>'
        else:
            subcategory_html += f'<div class="ag-check-box cb-category" for="{subcategory["category"]}"><span><input type="checkbox" name="subcategory" id="id_subcategory" value="{subcategory["slug"]}"><span class="checkbox-label">{subcategory["name"]}</span></span></div>'
    current_post_form['fields'][0] = {**current_post_form['fields'][0], 'categories': category_html}
    current_post_form['fields'][1] = {**current_post_form['fields'][1], 'subcategories': subcategory_html}



edit_post_form_2 = {

    'fields': [
        {'name': 'category', 'block': 'category_list'},
        {'name': 'subcategory', 'block': 'subcategory_list'},
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