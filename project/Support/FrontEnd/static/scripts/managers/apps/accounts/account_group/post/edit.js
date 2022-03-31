import { Form } from './../../../../forms/form.js'


document.addEventListener('DOMContentLoaded', makeValidation)


class EditPostForm extends Form {
    addMoreEvents = () => {
        let formButtons = document.querySelectorAll('button.bl-wh[type="submit"]')
        formButtons.forEach((btn) => {
            btn.addEventListener('click', (e) => {
                let btn = e.currentTarget
                this.formLabel = btn.querySelector('#submit-span')
            })
        })
    }
    startAnimation = () => {
        this.formLabel.innerHTML = ''
        this.formLabel.classList.add('btn-load-animation')
    }
}


function makeValidation() {

    let fieldsObj = {

        stringFields: [
            ['title', [['maxLength', 256]]],
            ['description', [['maxLength', 256]]],
        ],
        checkboxes: ['subcategory']

    }


    let form = new EditPostForm('form#edit-post-form', fieldsObj)
    form.addEvents()
    form.addMoreEvents()
}