import { clearError, clearSpaces } from './../../forms/clearInput.js'
import { formValidator } from './../../features/formValidation/validation.js'


export class Form {

    constructor(formElement, fieldsObj) {

        // web elements
        this.formElement = document.querySelector(formElement)
        this.textInputs = document.querySelectorAll('input[type="text"]')
        this.passwordInputs = document.querySelectorAll('input[type="password"]')

        // variables
        this.fieldsObj = fieldsObj

    }

    addEvents = () => {

        this.textInputs.forEach((input) => {
            input.addEventListener('focus', clearError)
        })
        
        
        this.passwordInputs.forEach((input) => {
            input.addEventListener('focus', clearError)
        })
        
        
        this.textInputs.forEach((input) => {
            input.addEventListener('blur', clearSpaces)
        })
        
        
        this.passwordInputs.forEach((input) => {
            input.addEventListener('blur', clearSpaces)
        })

        this.formElement.addEventListener('submit', this.validateForm)

    }

    validateForm = (event) => {
        let isValid = formValidator(this.fieldsObj)
        
        if (!isValid){
            event.preventDefault()
        }
    }

}