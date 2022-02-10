import { endAnimation } from '../../../../features/components/main/loadAnimation.js'
document.addEventListener('DOMContentLoaded', () => {endAnimation()})
import { FormWithUseJavascript } from './formModel.js'

document.addEventListener('DOMContentLoaded', makeValidation)


function makeValidation() {
    let fieldsObj = {
        stringFields: [
            ['email', []],
            ['password', []],
        ]
    }


    let form = new FormWithUseJavascript('form', fieldsObj)
    form.addEvents()
}