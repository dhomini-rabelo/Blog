import { endAnimation } from '../../../../features/components/main/loadAnimation.js'
document.addEventListener('DOMContentLoaded', () => {endAnimation()})

import { FormWithUseJavascript } from './formModel.js'


makeValidation()

function makeValidation() {

    let fieldsObj = {
        stringFields: [
            ['name', [['onlyStr'], ['maxLength', 256]]],
            ['email', [['maxLength', 128], ['email']]],
            ['password', [['minLength', 8], ['maxLength', 256]]],
            ['confirm_password', [['equalTheAField', 'password', 'As senhas']]],
        ]
    }

    let form = new FormWithUseJavascript('form[for="/cadastro/"]', fieldsObj)
    form.removeEvents()
    form.addEvents()
}