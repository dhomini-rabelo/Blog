# django
from django.utils.html import format_html


class Form:

    def __init__(self):
        self.form_fields = []
        self.form = ''
        self.error_space_html = '<div class="error">'
        self.error_message_format = '<span class="error-message"><img src="/static/admin/img/icon-no.svg" alt="error-img"></span>'
        self.error_message_space_html = '<span class="error-message"><img src="/static/admin/img/icon-no.svg" alt="error-img">'

    def form_for_save(self):
        return self.form_fields[:]
    
    def fast_load_form(self, form_fields: list[dict], processed_form: str):
        self.form_fields = [item.copy() for item in form_fields]
        self.form = processed_form[:]

    def load_form(self, form_fields: list[dict]):
        self.form_fields = [item.copy() for item in form_fields]
        self._update_form()
    
    def load_form_with_values(self, form_fields: list[dict], values: dict):
        copy_form_fields = [item.copy() for item in form_fields]
        for field in copy_form_fields:
            if field['name'] in values.keys():
                field['html'] = field['html'].replace('<input', f'<input value="{values[field["name"]]}"')
        self.form_fields = copy_form_fields
        self._update_form()
        
    def _update_form(self):
        self.form = ''.join(map(lambda field: field["html"], self.form_fields))

    def add_field(self, field: dict, structure: str, changes=[('[name]', 'name'), ('[label]', 'label'), ('[placeholder]', 'placeholder')]):
        for place, key in changes:
            structure.replace(place, field[key])

        self.form_fields.append({'name': field['name'], 'html': structure})
        self._update_form()

    def add_fields(self, fields: list[dict], structure: str, changes=[('[name]', 'name'), ('[label]', 'label'), ('[placeholder]', 'placeholder')]):
        for field in fields:
            field_structure = structure[:]
            for place, key in changes:
                field_structure = field_structure.replace(place, field[key])
            self.form_fields.append({'name': field['name'], 'html': field_structure}) 
        self._update_form()

    def show_errors(self, errors: dict):
        for input in self.form_fields:
            if input['name'] in errors.keys():
                input['html'] = input['html'].replace(self.error_space_html, f'{self.error_space_html}{self.error_message_format}').replace(self.error_message_space_html, f'{self.error_message_space_html}{errors[input["name"]]}')
        self._update_form()


    def clear_form(self):
        self.form = ''

    def change_error_html(self, error_content: str, error_message_html: str, error_space: str):
        """
        self.error_space_html => div
        self.error_message_space_html => span
        """
        self.error_space_html = error_content
        self.error_message_format = error_message_html
        self.error_message_space_html = error_space

    def get_form(self):
        return format_html(self.form)  



class BlocksForm:

    def __init__(self):
        self.form_fields = []
        self.form = ''
        self.error_space_html = '<div class="error">'
        self.error_message_format = '<span class="error-message"><img src="/static/admin/img/icon-no.svg" alt="error-img"></span>'
        self.error_message_space_html = '<span class="error-message"><img src="/static/admin/img/icon-no.svg" alt="error-img">'

    def form_for_save(self):
        return self.form_fields[:]
    
    def fast_load_form(self, form_fields: list[dict], processed_form: str):
        self.form_fields = [item.copy() for item in form_fields]
        self.form = processed_form[:]

    def load_form(self, form_fields: list[dict]):
        self.form_fields = [item.copy() for item in form_fields]
        self._update_form()
    
    def load_form_with_values(self, form_fields: list[dict], values: dict):
        copy_form_fields = [item.copy() for item in form_fields]
        for field in copy_form_fields:
            if field['name'] in values.keys():
                field['html'] = field['html'].replace('<input', f'<input value="{values[field["name"]]}"')
        self.form_fields = copy_form_fields
        self._update_form()
        
    def _update_form(self):
        self.form = ''.join(map(lambda field: field["html"], self.form_fields))

    def add_field(self, field: dict, structure: str, changes=[('[name]', 'name'), ('[label]', 'label'), ('[placeholder]', 'placeholder')]):
        for place, key in changes:
            structure.replace(place, field[key])

        self.form_fields.append({'name': field['name'], 'html': structure, 'settings': field.get('settings')})
        self._update_form()

    def add_fields(self, fields: list[dict], structure: str, changes=[('[name]', 'name'), ('[label]', 'label'), ('[placeholder]', 'placeholder')]):
        for field in fields:
            field_structure = structure[:]
            for place, key in changes:
                field_structure = field_structure.replace(place, field[key])
            self.form_fields.append({'name': field['name'], 'html': field_structure, 'settings': field.get('settings')}) 
        self._update_form()

    def show_errors(self, errors: dict):
        
        fields_name = list(map(lambda field: field['name'][:], self.form_fields))
        
        for error_key in errors.keys():
            if error_key in fields_name:
                error_position = fields_name.index(error_key)
                field = self.form_fields[error_position]
                field['html'] = field['html'].replace(self.error_space_html, f'{self.error_space_html}{self.error_message_format}').replace(self.error_message_space_html, f'{self.error_message_space_html}{errors[field["name"]]}')
        
        # for input in self.form_fields:
        #     if input['name'] in errors.keys():
        #         input['html'] = input['html'].replace(self.error_space_html, f'{self.error_space_html}{self.error_message_format}').replace(self.error_message_space_html, f'{self.error_message_space_html}{errors[input["name"]]}')
        self._update_form()


    def clear_form(self):
        self.form = ''

    def change_error_html(self, error_content: str, error_message_html: str, error_space: str):
        """
        self.error_space_html => div
        self.error_message_space_html => span
        """
        self.error_space_html = error_content
        self.error_message_format = error_message_html
        self.error_message_space_html = error_space

    def get_form(self):
        return format_html(self.form)  
