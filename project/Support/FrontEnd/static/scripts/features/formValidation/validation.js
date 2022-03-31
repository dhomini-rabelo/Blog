import {validateStringField} from './validators/string.js'
import {validateCheckBox} from './validators/checkbox.js'

export function formValidator(formObj){
    let valid = true

    for (let stringField of formObj.stringFields || []){
        let validation = validateStringField(stringField)
        if (!validation){
            valid = false
        }
    }

    for (let checkboxField of formObj.checkboxes || []){
        let validation = validateCheckBox(checkboxField)
        if (!validation){
            valid = false
        }
    }

    return valid
}