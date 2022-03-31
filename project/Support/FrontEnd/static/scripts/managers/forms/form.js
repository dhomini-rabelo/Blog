import { clearError, clearSpaces } from './../../forms/clearInput.js'
import { formValidator } from './../../features/formValidation/validation.js'


export class Form {

    constructor(formElement, fieldsObj) {

        // web elements
        this.formAddress = formElement
        this.formElement = document.querySelector(formElement)
        this.textInputs = this.formElement.querySelectorAll('input[type="text"]')
        this.passwordInputs = this.formElement.querySelectorAll('input[type="password"]')
        this.checkBoxes = this.formElement.querySelectorAll('input[type="checkbox"]')

        // variables
        this.fieldsObj = fieldsObj
    }

    removeEvents = () => {

        this.textInputs.forEach((input) => {
            input.removeEventListener('focus', clearError)
        })
        
        
        this.passwordInputs.forEach((input) => {
            input.removeEventListener('focus', clearError)
        })
        
        
        this.textInputs.forEach((input) => {
            input.removeEventListener('blur', clearSpaces)
        })
        
        
        this.passwordInputs.forEach((input) => {
            input.removeEventListener('blur', clearSpaces)
        })

        this.checkBoxes.forEach((input) => {
            input.removeEventListener('change', clearError)
        })

        let forms = document.querySelectorAll('form')
        forms.forEach((form) => {
            form.removeEventListener('submit', self.validateForm)
        })

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

        this.checkBoxes.forEach((input) => {
            input.addEventListener('change', clearError)
        })

        this.formElement.addEventListener('submit', this.validateForm)

    }

    validateForm = (event) => {
        event.preventDefault()
        let isValid = formValidator(this.fieldsObj)
        if (!isValid){
            event.preventDefault()
        } else {
            this.startAnimation()
        }
    }

    startAnimation = () => {
        let button = document.querySelector('#submit-span')
        button.innerHTML = ''
        button.classList.add('btn-load-animation')
    }

}