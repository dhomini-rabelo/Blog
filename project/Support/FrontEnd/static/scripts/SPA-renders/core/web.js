export function changeUrl(title, newUrl) {
    window.history.pushState({}, "", `${newUrl}`)
    document.title = title
}



export function render(local, changes) {
    let localForChanges = document.querySelector(local)
    
    controlGroupStyles(changes.newHead.group)
    removeAllStyles('head .styles-individual')
    addStyles('head .styles-individual', changes.newHead.individualStyles)

    localForChanges.innerHTML = changes.newContent

    addScripts(changes.newScripts)
}

