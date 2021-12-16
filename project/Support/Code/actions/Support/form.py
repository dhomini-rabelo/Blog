# django
from django.utils.html import format_html
# this module
from .support import adapt_form_errors, adapt_list_of_post_form
from .functions_dict import convert_functions, other_errors_functions
from .checks import check_null
from .utils import gets
# others
from decimal import InvalidOperation
from typing import Sequence, Union, Any
from pprint import pprint



def validate_form(post_form, *fields, default_type='str', default_validation=[('max_length', 256)]):
    def get_field(field):
        if isinstance(field, str):
            return field
        elif isinstance(field, list):
            return field[0]
    fields_name = list(map(get_field, fields)) 
    form_fields = gets(post_form, *fields_name)

    form_fields_adapted_format = []
    for index, field_format in enumerate(fields):
        field_adapted = []

        field_format = field_format if isinstance(field_format, list) else [field_format]

        match len(field_format):
            case 1:
                field_adapted = [form_fields[index], default_type, fields_name[index], default_validation]
            case 2:
                if isinstance(field_format[1], str):
                    field_adapted = [form_fields[index], field_format[1], fields_name[index], default_validation]
                elif isinstance(field_format[1], list):
                    field_adapted = [form_fields[index], default_type, fields_name[index], field_format[1]]
            case 3: 
                field_adapted = [form_fields[index], field_format[1], fields_name[index], field_format[2]]

        form_fields_adapted_format.append(field_adapted)

    errors = get_post_form_errors(form_fields_adapted_format)

    fields_value = {}

    for field in form_fields_adapted_format:
        fields_value[field[2]] = field[0]

    if errors is None:
        return {'status': 'valid', 'errors': {}, 'fields': fields_value}
    else:
        return {'status': 'invalid', 'errors': errors, 'fields': fields_value}





def convert(obj: str, new_type: str):
    convert_process = convert_functions[new_type]
    
    if obj is not None:
        return convert_process(obj)
    else:
        return None



def convert_validation(field: Any, new_type: str):
    if new_type == 'pass': return 'valid'
    try:
        validation = convert(field, new_type)
        return validation if validation is not None else 'convert_error'
    except (ValueError, InvalidOperation):
        return 'convert_error'
        
        

     
        
        
def get_post_form_errors(form: list) -> dict[str, str]:
    """
    Form list fields
    [
    [value, type, field_name, [(other_validation, *args),]],
    ]
    """
    # errors
    invalid_fields, none_fields, other_errors = [], [], []
    types_for_others_validations = [
        'unique', 'unique_m2m_or_custom','exists', 'only_str', 'only_numeric', 'email', 'caracters',
        'min-max-equal(length)', 'username', 'slug',
    ]
    
    for field, convert_var, name, more_validations in adapt_list_of_post_form(form):
        formated_field = convert_validation(field, convert_var)

        if check_null(field):
            none_fields.append(name)  
        elif str(formated_field) == 'convert_error':
            invalid_fields.append(name)
        else:
            for other_validation in more_validations:
                args = [*other_validation[1:]]
                args.insert(0, formated_field)
                validation = other_errors_functions[other_validation[0]]
                if not validation(*args):
                    other_errors.append([other_validation[0], name, args])
                
    form_errors = {'invalid_fields': invalid_fields, 'none_fields': none_fields,
                    'other_errors': other_errors}
    
    form_errors = adapt_form_errors(form_errors)
    return form_errors if form_errors != {} else None


    
def get_password_error(password: str, confirm_password: str):
    if not password == confirm_password:
        return 'As senhas são diferentes'
    return None


def change_password(user, current_password: str, new_password: str, new_password_confirm: str) -> str:
    if not user.check_password(current_password):
        error = 'Senha incorreta'
        return error
    else:
        error_password = get_password_error(new_password, new_password_confirm)
        if error_password is None:
            user.set_password(new_password)
            user.save()
            return 'success'
        else:
            error = error_password
            return error
    



class Form:

    def __init__(self):
        self.form_fields = []
        self.form = ''
        self.error_space_html = '<div class="error">'
        self.error_message_format = '<img src="/static/admin/img/icon-no.svg" alt="error-img"><span class="error-message"></span>'
        self.error_message_space_html = '<span class="error-message">'

    def form_for_save(self):
        return self.form_fields

    def load_form(self, form_fields: list[dict]):
        self.form_fields = form_fields
        self._update_form()
    
    def load_form_with_values(self, form_fields: list[dict], values: dict):
        print(values)
        for field in form_fields:
            if field['name'] in values.keys():
                field['html'] = field['html'].replace('<input', f'<input value="{values[field["name"]]}"')
        self.form_fields = form_fields
        self._update_form() 
        

    def _update_form(self):
        self.form = ''
        for field in self.form_fields:
            self.form += field['html']

    def add_field(self, field: dict, structure: str, changes=[('[name]', 'name'), ('[label]', 'label')]):
        for place, key in changes:
            structure.replace(place, field[key])

        self.form_fields.append({'name': field['name'], 'html': structure})
        self._update_form()

    def add_fields(self, fields: list[dict], structure: str, changes=[('[name]', 'name'), ('[label]', 'label')]):
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
        self.clear_form()
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

