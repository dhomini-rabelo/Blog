export function clearError(event){
    let input = event.currentTarget
    input.parentElement.querySelector('.error').innerHTML = ''
}

export function clearField(fieldElement){
    fieldElement.parentElement.querySelector('.error').innerHTML = ''
}

export function clearSpaces(event){
    let input = event.currentTarget
    input.value = input.value.trim()
}