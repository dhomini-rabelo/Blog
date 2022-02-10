import { formValidator } from './../../../../features/formValidation/validation.js'
import { Form } from './../../../forms/form.js'


export class FormWithUseJavascript extends Form {
    validateForm = (event) => {
        let useJavascript = document.querySelector('#id_javascript')
        if (!useJavascript.checked){return}
        
        let isValid = formValidator(this.fieldsObj)
        
        if (!isValid){
            event.preventDefault()
        }
    }
}