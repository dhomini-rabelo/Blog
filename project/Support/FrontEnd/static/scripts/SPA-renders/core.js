export function changeUrl(title, newUrl) {
    window.history.pushState({}, "", `${newUrl}`)
    document.title = title
}

export function addStyles(newStyles) {
    let head = document.querySelector('head')
    head.innerHTML = `
    ${head.innerHTML}
    ${newStyles.map((style) => {
        let weStyle = document.querySelector(`link[href="${style}"]`)
        return weStyle ? '' : `<link rel="stylesheet" href="${style}">`
    })}
    `
}

export function removeStyles(oldStyles) {
    oldStyles.forEach((style) => {
        let weStyle = document.querySelector(`link[href="${style}"]`)
        if(weStyle) {
            weStyle.remove()
        }
    })
}

export function addScripts (newScripts) {
    let body = document.querySelector('body')

    for (let [scriptSource, isModule=false] of newScripts) {
        let checkExists = document.querySelector(`script[src="${scriptSource}"]`)
        if (!checkExists) {
            let newScript = document.createElement('script')
            newScript.setAttribute('src', scriptSource)
            if(isModule) {
                newScript.setAttribute('type', 'module')
            }
            body.appendChild(newScript)
        }
    }
}

export function render(local, changes) {
    let localForChanges = document.querySelector(local)
    let head = document.querySelector('head')
    
    head.innerHTML = changes.newHead
    localForChanges.innerHTML = changes.newContent
    addScripts(changes.newScripts)
}
