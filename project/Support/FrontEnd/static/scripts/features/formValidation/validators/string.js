import { validateStringLength, validateEmail, validateEqualTheAField } from './support/string.js'
import { showError } from '../createError.js'

export function validateStringField(fieldModel){

    let valid = true
    let field = document.querySelector(`input#id_${fieldModel[0]}`)
    let validations = fieldModel[1]
    let errorMessage = ''

    if (field.value.trim().length === 0){
        valid = false
        errorMessage = 'Este campo é obrigatório'
    }


    if (valid){

        for (let validation of validations){
            let validationProcess
            let validationType = validation[0]
    
            switch (validationType){
                case 'maxLength':
                    validationProcess = validateStringLength('max', field.value, validation[1])
                    if (!validationProcess){
                        errorMessage = `Este campo deve ter no máximo ${validation[1]} dígitos`
                    }
                    break
                case 'equalLength':
                    validationProcess = validateStringLength('equal', field.value, validation[1])
                    if (!validationProcess){
                        errorMessage = `Este campo deve ter ${validation[1]} dígitos`
                    }
                    break
                case 'minLength':
                    validationProcess = validateStringLength('min', field.value, validation[1])
                    if (!validationProcess){
                        errorMessage = `Este campo deve ter no mínimo ${validation[1]} dígitos`
                    }
                    break
                case 'email':
                    validationProcess = validateEmail(field.value)
                    if (!validationProcess){
                        errorMessage = `Email inválido`
                    }
                    break
                case 'equalTheAField':
                    validationProcess = validateEqualTheAField(field.value, `#id_${validation[1]}`)
                    if (!validationProcess){
                        errorMessage = `${validation[2]} são diferentes`
                    }
                    break
            }
    
            if (!validationProcess){
                valid = false
            }

        }

    }

    if (!valid){
        showError(field.parentElement.querySelector('.error'), errorMessage)
    }

    return valid
}