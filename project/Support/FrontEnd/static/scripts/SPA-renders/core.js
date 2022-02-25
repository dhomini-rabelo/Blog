export function changeUrl(title, newUrl) {
    window.history.pushState({}, "", `${newUrl}`)
    document.title = title
}

export function addStyles(local, hrefAddresses) {
    let weLocal = document.querySelector(local)
    if(!weLocal) return

    for (let hrefLink of hrefAddresses){
        if (document.querySelector(`link[href="${hrefLink}"]`) !== null) continue
        let newLink = document.createElement('link')
        newLink.setAttribute('rel', 'stylesheet')
        newLink.setAttribute('href', hrefLink)
        weLocal.append(newLink)
    }
}

export function controlGroupStyles (group) {
    let currentStyles
    let mainStyles = [
        '/static/styles/_compacts/min/main.min.css',
    ]
    let accountStyles = [
        '/static/styles/_compacts/min/main.min.css',
        '/static/styles/_compacts/min/account.min.css',
    ]
    switch (group){
        case 'main':
            currentStyles = mainStyles
            break
        case 'account':
            currentStyles = accountStyles
            break
        case _:
            throw new Error('Invalid Group')
    }
    let groupStyles = document.querySelectorAll('head .styles-group link[rel="stylesheet"]')

    groupStyles.forEach((style) => {
        if (!(In(style.getAttribute('href'), currentStyles))){
            style.remove()
        }
    })
    addStyles('head .styles-group', currentStyles)
}
 


export function removeStyles(oldStyles) {
    oldStyles.forEach((style) => {
        let weStyle = document.querySelector(`link[href="${style}"]`)
        if(weStyle) {
            weStyle.remove()
        }
    })
}

export function removeAllStyles (local) {
    let weLocal = document.querySelector(local)
    if(!weLocal) return
    let styles = weLocal.querySelectorAll('link[rel="stylesheet"]')
    styles.forEach(style => style.remove())
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
    
    controlGroupStyles(changes.newHead.group)
    removeAllStyles('head .styles-individual')
    addStyles('head .styles-individual', changes.newHead.individualStyles)

    localForChanges.innerHTML = changes.newContent
    addScripts(changes.newScripts)
}

export function disableTagsA() {
    let allTagsA = document.querySelectorAll('a')
    allTagsA.forEach((a) => a.addEventListener('click', (e) => e.preventDefault()))
}

export function enableTagsA() {
    let allTagsA = document.querySelectorAll('a')
    allTagsA.forEach((a) => a.removeEventListener('click', (e) => e.preventDefault()))
}