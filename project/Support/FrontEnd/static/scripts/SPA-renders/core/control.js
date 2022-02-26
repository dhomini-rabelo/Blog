import { In } from './../../features/core/utils.js'
import { addStyles } from './styles.js'
import { addScriptsGroup } from './scripts.js'



export function controlGroupStyles (styles) {
    let groupStyles = document.querySelectorAll('.styles-group link[rel="stylesheet"]')

    groupStyles.forEach((style) => {
        if (!(In(style.getAttribute('href'), styles))){
            style.remove()
        }
    })
    addStyles('.styles-group', styles)
}



export function controlGroupScripts(scriptTypes){
    let scriptGroups = document.querySelectorAll('.scripts')
    let currentScriptsGroup = []

    scriptGroups.forEach((scriptGroup) => {
        let groupType = scriptGroup.getAttribute('type')
        if (!(In(groupType, scriptTypes))){
            scriptGroup.remove()
        }else{
            currentScriptsGroup.push(groupType)
        }
    })

    scriptTypes.forEach((type) => {if (!(In(type, currentScriptsGroup))) addScriptsGroup(type)})
}
