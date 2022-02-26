export function addStyles(local, hrefAddresses) {
    let weLocal = document.querySelector(local)
    if(!weLocal) return

    for (let hrefLink of hrefAddresses){
        if (document.querySelector(`link[href="${hrefLink}"]`))  continue
        let newLink = document.createElement('link')
        newLink.setAttribute('rel', 'stylesheet')
        newLink.setAttribute('href', hrefLink)
        weLocal.append(newLink)
    }
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