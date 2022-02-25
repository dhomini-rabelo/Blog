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




export function controlGroupScripts(group){
    let scriptGroups = document.querySelectorAll('.scripts')
    
    let currentScripts

    let mainScripts = {
        locals: [
            'scripts-main-group'
        ],
        scripts: [
            '/static/styles/_compacts/min/main.min.css',
        ]
    }

    let accountScripts = {
        locals: [
            'scripts-account-group', 'scripts-main-group'
        ],
        scripts: [
            '/static/styles/_compacts/min/main.min.css',
        ]
    }


    switch (group){
        case 'main':
            currentScripts = { ...mainScripts }
            break
        case 'account':
            currentScripts = { ...accountScripts }
            break
        case _:
            throw new Error('Invalid Group')
    }

    scriptGroups.forEach((script) => {
        let scriptSrc = script.getAttribute('src')
        if (!(In(scriptSrc, currentScripts.locals))){
            removeScripts(currentScript)
        }
    })

}
 