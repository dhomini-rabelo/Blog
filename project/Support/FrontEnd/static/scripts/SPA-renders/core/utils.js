export function disableTagsA() {
    let allTagsA = document.querySelectorAll('a')
    allTagsA.forEach((a) => a.addEventListener('click', (e) => e.preventDefault()))
}

export function enableTagsA() {
    let allTagsA = document.querySelectorAll('a')
    allTagsA.forEach((a) => a.removeEventListener('click', (e) => e.preventDefault()))
}



export function addContent(group, page) {
    let spaGroup = JSON.parse(document.querySelector('#SPGT').value)

    return spaGroup[group][page]
}