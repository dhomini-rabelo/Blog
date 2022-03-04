import { microsSPA } from './settings.js'
import { controlGroupStyles } from './control.js'
import { removeAllStyles, addStyles } from './styles.js'
import { removeAllScripts, addScripts } from './scripts.js'
import { addContent } from './utils.js'





export function changeUrl(title, newUrl) {
    localStorage.setItem('back', window.location.pathname)
    window.history.pushState(null, "", `${newUrl}`)
    document.title = title
}


export function render(local, changes, SPGT=true) {
    let localForChanges = document.querySelector(local)
    let spa = microsSPA[changes.group]
    
    controlGroupStyles(spa.styles)
    removeAllStyles('.styles-individual')
    addStyles('.styles-individual', changes.individualStyles)

    if (SPGT){
        localForChanges.innerHTML = addContent(changes.group, changes.content)
    } else {
        localForChanges.innerHTML = changes.content
    }
    
    addScripts('.scripts-individual', changes.individualScripts)
}
