# this module
from support import adapt_form_errors, adapt_list_of_post_form
from functions_dict import convert_functions, other_errors_functions
from checks import check_null
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
        
        

field_sequence_for_validation = Sequence[Any, str, str, list[tuple[str, Any]]]
form_type = list[list[field_sequence_for_validation]]      
        
        
def get_post_form_errors(form: form_type) -> dict[str, str]:
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
    

