import { Form } from './../../../../forms/form.js'


document.addEventListener('DOMContentLoaded', makeValidation)


function makeValidation() {

    let fieldsObj = {

        stringFields: [
            ['name', [['onlyStr'], ['maxLength', 256]]],
        ]

    }


    let form = new Form('form.ag-form', fieldsObj)
    form.addEvents()
}