import {validateStringField} from './validators/string.js'

export function formValidator(formObj){
    let valid = true

    for (let stringField of formObj.stringFields){
        let validation = validateStringField(stringField)
        if (!validation){
            valid = false
        }
    }

    return valid
}