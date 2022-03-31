import { showError } from '../createError.js'

export function validateCheckBox(inputName){
    let inputs = document.querySelectorAll(`#id_${inputName}`)
    let valid = false
    inputs.forEach((input) => {
        if (input.checked === true){
            valid = true
        }
    })
    if (valid === false) {
        showError(document.querySelector(`#id_${inputName}`).parentElement.parentElement.parentElement.querySelector('.error'), 'Nenhuma opção foi marcada')
    }
    return valid
}