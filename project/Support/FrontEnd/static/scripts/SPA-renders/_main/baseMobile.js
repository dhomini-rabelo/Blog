import { renderSPA } from './base.js'


let mobileNavigationFields = document.querySelectorAll('.mobile-footer .navigation')


mobileNavigationFields.forEach((field) => {
    field.addEventListener('click', renderNewPage)
})


function renderNewPage(e) {
    let navigationField = e.currentTarget
    let destiny = navigationField.getAttribute('id').slice(0, -5)

    if (destiny !== 'account'){
        e.preventDefault()
        renderSPA(destiny)
    }
}
