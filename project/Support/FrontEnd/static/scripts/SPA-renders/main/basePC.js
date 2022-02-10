import { renderSPA } from './base.js'

let pcNavigationFields = document.querySelectorAll('.sub-menu .pc-link-navigation')


pcNavigationFields.forEach((field) => {
    field.addEventListener('click', renderNewPagePc)
})


function renderNewPagePc(e){
    let navigationField = e.currentTarget
    let destiny = navigationField.getAttribute('destiny')

    if (destiny !== 'pass'){
        e.preventDefault()
        renderSPA(destiny)
    }
}