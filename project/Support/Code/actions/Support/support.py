# this module
from functions_dict import messages_form_errors


def adapt_form_errors(form_errors: dict[str, list]) -> dict[str, str]:
    response = dict()
    for name in form_errors['invalid_fields']:
        response[name] = 'Este campo é inválido'
    for name in form_errors['none_fields']:
        response[name] = 'Este campo é obrigatório'
    for error, name, args in form_errors['other_errors']:
        if error in ['min_length', 'equal_length', 'max_length']:
            response[name] = messages_form_errors[error](args[1])
        else:
            response[name] = messages_form_errors[error]
    return response



def adapt_list_of_post_form(post_form_list: list):
    new_list = []
    for form_list in post_form_list:
        if len(form_list) == 3:
            model = form_list[:]
            model.append([])
            new_list.append(model)
        else:
            new_list.append(form_list)
    return new_list


