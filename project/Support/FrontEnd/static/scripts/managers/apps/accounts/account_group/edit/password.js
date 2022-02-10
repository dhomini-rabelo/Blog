import { Form } from './../../../../forms/form.js'


document.addEventListener('DOMContentLoaded', makeValidation)


function makeValidation() {

    let fieldsObj = {

        stringFields: [
            ['current_password', []],
            ['new_password', [['minLength', 8], ['maxLength', 256]]],
            ['confirm_new_password', [['equalTheAField', 'new_password', 'As senhas']]],
        ]

    }


    let form = new Form('form#password_form', fieldsObj)
    form.addEvents()
}