import { formValidator } from './../../features/formValidation/validation.js'
import { clearError, clearSpaces } from './../../forms/clearInput.js'

let textInputs = document.querySelectorAll('input[type="text"]')
let passwordInputs = document.querySelectorAll('input[type="password"]')



textInputs.forEach((input) => {
    input.addEventListener('focus', clearError)
})


passwordInputs.forEach((input) => {
    input.addEventListener('focus', clearError)
})


textInputs.forEach((input) => {
    input.addEventListener('blur', clearSpaces)
})


passwordInputs.forEach((input) => {
    input.addEventListener('blur', clearSpaces)
})


document.querySelector('form').addEventListener('submit', validateForm)



function validateForm(event){
    let useJavascript = document.querySelector('#id_javascript')
    if (!useJavascript.checked){return}
    
    let formObj = {
        'str': [
            ['name', [['maxLength', 256]]],
            ['email', [['maxLength', 128], ['email']]],
            ['password', [['minLength', 8], ['maxLength', 256]]],
            ['confirm_password', [['equalTheAField', 'password', 'As senhas']]],
        ]
    }
    
    let isValid = formValidator(formObj)

    
    if (!isValid){
        event.preventDefault()
    }
}
