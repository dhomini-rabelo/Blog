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