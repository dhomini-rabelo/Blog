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
    let inputForCopy = document.querySelector(inputForCopyAddress).value

    return inputForCopy === inputValue ? true : false
}