import { scriptsSPA } from './settings.js'


export function addScripts (local, newScripts) {
    let weLocal = document.querySelector(local)
    if(!weLocal) return

    for (let [scriptSource, isModule=false] of newScripts) {
        let checkExists = document.querySelector(`script[src="${scriptSource}"]`)
        if (!checkExists) {
            let newScript = document.createElement('script')
            newScript.setAttribute('src', scriptSource)
            if(isModule) {
                newScript.setAttribute('type', 'module')
            }
            weLocal.appendChild(newScript)
        }
    }
}

export function addScriptsGroup(type) {
    if(document.querySelector(`div[type="${type}"]`)) return
    let body = document.querySelector('body')
    let groupScripts = scriptsSPA[type]

    let groupContainer = document.createElement('div')
    groupContainer.setAttribute('class', 'scripts')
    groupContainer.setAttribute('type', type)
    body.appendChild(groupContainer)

    addScripts(`div[type="${type}"]`, groupScripts)

}


export function removeAllScripts(local) {
    let weLocal = document.querySelector(local)
    if(!weLocal) return
    let scripts = weLocal.querySelectorAll('script')
    scripts.forEach(script => script.remove())
}