# django
from django.utils.html import format_html
# this module
from .support import adapt_form_errors, adapt_list_of_post_form
from .functions_dict import convert_functions, other_errors_functions
from .checks import check_null
# others
from decimal import InvalidOperation
from typing import Sequence, Union, Any





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
        
        

     
        
        
def get_post_form_errors(form: dict) -> dict[str, str]:
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

    def _update_form(self):
        for field in self.form_fields:
            self.form += field['html']

    def add_charfields(self, fields: list, structure: str):
        for field in fields:
            self.form_fields.append({'name': field['name'], 'html': structure.replace('[name]', field['name']).replace('[label]', field['label'])})
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






