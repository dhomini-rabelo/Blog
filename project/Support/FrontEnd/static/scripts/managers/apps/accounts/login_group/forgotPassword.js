import { endAnimation } from '../../../../features/components/main/loadAnimation.js'
import { Form } from './../../../forms/form.js'


document.addEventListener('DOMContentLoaded', () => {endAnimation()})
document.addEventListener('DOMContentLoaded', makeValidation)


function makeValidation() {

    let fieldsObj = {

        stringFields: [
            ['new_password', [['minLength', 8], ['maxLength', 256]]],
            ['confirm_new_password', [['equalTheAField', 'new_password', 'As senhas']]],
        ]

    }


    let form = new Form('form', fieldsObj)
    form.addEvents()
}