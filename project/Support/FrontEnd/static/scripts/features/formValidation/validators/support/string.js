export function validateStringLength(type, text, length){
    switch (type){
        case 'max':
            return text.length <= length ? true : false
        case 'equal':
            return text.length === length ? true : false
        case 'min':
            return text.length >= length ? true : false
    }
}

export function validateEmail(email){
    if (email.indexOf('@')!==-1){
        let sliceEmail = email.substring(email.indexOf('@'))
        for (let emailLetter of sliceEmail){
            if (emailLetter === '.' && sliceEmail.indexOf(emailLetter) !== sliceEmail.length){
                return true
            }
        }
    }
    return false
}

export function validateEqualTheAField(inputValue, inputForCopyAddress){
    console.log(inputForCopyAddress)
    let inputForCopy = document.querySelector(`#id_${inputForCopyAddress}`).value

    return inputForCopy === inputValue ? true : false
}


export function validateCPF(inputValue){
    let cpfRegexExpression = /^\d{3}\.\d{3}\.\d{3}-\d{2}$/
    
    return inputValue.match(cpfRegexExpression) === null ? false : true
}

export function onlyLetters(inputValue){
    let onlyLettersRegexExpression = /^[a-zA-z\sáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ]+$/

    return inputValue.match(onlyLettersRegexExpression) === null ? false : true
}


export let StringValidationObj = {

    maxLength: (fieldValue, length_) => validateStringLength('max', fieldValue, length_),
    equalLength: (fieldValue, length_) => validateStringLength('equal', fieldValue, length_),
    minLength: (fieldValue, length_) => validateStringLength('min', fieldValue, length_),
    email: validateEmail,
    equalTheAField: validateEqualTheAField,
    cpf: validateCPF,
    onlyStr: onlyLetters,
}



export let StringErrorsObj = {

    maxLength: (length_) => `Este campo deve ter no máximo ${length_} dígitos`,
    equalLength: (length_) => `Este campo deve ter ${length_} dígitos`,
    minLength: (length_) => `Este campo deve ter no mínimo ${length_} dígitos`,
    equalTheAField: (fieldsName) => `${fieldsName} são diferentes`,
    email: 'Email inválido',
    cpf: 'CPF inválido',
    onlyStr: 'Este campo aceita apenas letras'    

}