import { microsSPA } from './settings.js'
import { controlGroupStyles } from './control.js'
import { removeAllStyles, addStyles } from './styles.js'





export function changeUrl(title, newUrl) {
    window.history.pushState({}, "", `${newUrl}`)
    document.title = title
}


export function render(local, changes) {
    let localForChanges = document.querySelector(local)
    let spa = microsSPA[changes.group]
    
    controlGroupStyles(spa.styles)
    removeAllStyles('.styles-individual')
    addStyles('.styles-individual', changes.individualStyles)

    localForChanges.innerHTML = changes.content
}

