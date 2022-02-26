import { In } from './../../'


export function controlGroupStyles (styles) {
    let groupStyles = document.querySelectorAll('head .styles-group link[rel="stylesheet"]')

    groupStyles.forEach((style) => {
        if (!(In(style.getAttribute('href'), styles))){
            style.remove()
        }
    })
    addStyles('head .styles-group', styles)
}



export function controlGroupScripts(scriptTypes){
    let scriptGroups = document.querySelectorAll('.scripts')
    let currentScriptsGroup = []

    scriptGroups.forEach((scriptGroup) => {
        let groupType = scriptGroup.getAttribute('type')
        if (!(In(groupType, scriptTypes))){
            removeScriptsGroup(scriptSrc)
        }else{
            currentScriptsGroup.push(groupType)
        }
    })

    scriptTypes.forEach((type) => {if (!(In(type, currentScriptsGroup))) addScriptsGroup(type)})
}
