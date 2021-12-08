from validators import validate_unique, validate_for_email, validate_caracters, validate_for_slug, validate_only_numeric
from datetime import datetime
from decimal import Decimal


# for support

messages_form_errors = {
    'unique': 'Este campo já está em uso', 'exists': 'Este campo valor já foi cadastrado',
    'only_str': 'Este campo aceita apenas letras', 'only_numeric': 'Este campo aceita apenas números',
    'username': 'Este campo aceita apenas números, letras e underline',
    'min_length': lambda length: f'Este campo deve ter no mínimo {length} dígitos',
    'equal_length': lambda length: f'Este campo deve ter {length} dígitos',
    'max_length': lambda length: f'Este campo deve ter no máximo {length} dígitos',
    'slug': 'Este campo não pode ser representado por uma url, use apenas letras, hífen e underline',
    'email': 'Este email não está em um formato válido',
}




# for form

convert_functions = {
    'str': lambda obj: str(obj), 'int': lambda obj: int(obj), 'float': lambda obj: float(obj),
    'decimal': lambda obj: Decimal(obj), 'date': lambda obj: datetime.strptime(obj, '%d/%m/%Y').date(),
}


other_errors_functions = {
    # model
    'unique': lambda field, Model, field_name: validate_unique(Model, field_name, field),
    'unique_m2m_or_custom': lambda field, Model, field_name: validate_unique(Model, field_name, field, True),
    'exists': lambda field, Model, field_name: not validate_unique(Model, field_name, field),
    # format
    'only_str': lambda field: validate_caracters(field, True, True, False, False, False),
    'username': lambda field: validate_caracters(field, False, False, False),
    'only_numeric': lambda field: validate_only_numeric(field), 
    'decimal': lambda field: (validate_only_numeric(field[:-3]) and field[-3] == '.' and validate_only_numeric(field[-2:])),
    'equal_length': lambda field, length: len(str(field)) == length,
    'min_length': lambda field, length: len(str(field)) >= length,
    'max_length': lambda field, length: len(str(field)) <= length,
    # value
    'email': lambda field: validate_for_email(field),
    'slug': lambda field: validate_for_slug(field),
}


# for utils

def get_name(text: str):
    list_string = text.split(' ')
    text = [word.strip().title() for word in list_string if word != '']
    return " ".join(text)

def get_only_numbers(text: str):
    new_text = ''
    for letter in text:
        if letter in list('0123456789'):
            new_text += letter
    return new_text


def get_decimal_from_money_br(text: str):
    new_text = ''
    for letter in text:
        if letter in list('0123456789,'):
            new_text += letter
    return new_text.replace(',', '.')        



filters_functions = {
    'strip': lambda text: text.strip(), 'name': lambda text: get_name(text),
    'only_numbers': lambda text: get_only_numbers(text),
    'money_br': lambda text: get_decimal_from_money_br(text),
}