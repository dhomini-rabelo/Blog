import { Form } from './../../../../forms/form.js'


document.addEventListener('DOMContentLoaded', makeValidation)


function makeValidation() {

    let fieldsObj = {

        stringFields: [
            ['title', [['maxLength', 256]]],
            ['description', [['maxLength', 256]]],
        ],
        checkboxes: ['subcategory']

    }


    let form = new Form('form#create-post-form', fieldsObj)
    form.addEvents()
}