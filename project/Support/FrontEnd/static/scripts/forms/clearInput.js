export function clearError(event){
    let input = event.currentTarget
    if(!input) return
    let error = input.parentElement.querySelector('.error')
    if(!error) return
    error.innerHTML = ''
}

export function clearField(fieldElement){
    if(!fieldElement) return
    let error = fieldElement.parentElement.querySelector('.error')
    if(!error) return
    error.innerHTML = ''
}

export function clearSpaces(event){
    let input = event.currentTarget
    input.value = input.value.trim()
}