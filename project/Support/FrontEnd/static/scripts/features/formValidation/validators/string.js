import { StringValidationObj, StringErrorsObj } from './support/string.js'
import { clearField } from '../../../forms/clearInput.js'
import { showError } from '../createError.js'
import { In } from './../../core/utils.js'


export function validateStringField(fieldModel){

    let valid = true
    let field = document.querySelector(`input#id_${fieldModel[0]}`)
    clearField(field)
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
            let validateFunction = StringValidationObj[validationType]
    

            // 1 arg for validation
            if (In(validationType, ['maxLength', 'equalLength', 'minLength', 'equalTheAField'])){
                validationProcess = validateFunction(field.value, validation[1])
            } else {
                validationProcess = validateFunction(field.value)
            }
    
            if (!validationProcess){

                errorMessage = StringErrorsObj[validationType]

                if (In(validationType, ['maxLength', 'equalLength', 'minLength'])){
                    errorMessage = errorMessage(validation[1])
                } else if (In(validationType, ['equalTheAField'])) {
                    errorMessage = errorMessage(validation[2])
                }
                
                valid = false
                break
            }

        }
    }

    if (!valid){
        showError(field.parentElement.querySelector('.error'), errorMessage)
    }

    return valid
}