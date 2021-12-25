export function In(object, array){
    for (let item of array){
        if (object === item){
            return true
        }
    }
    return false
}

export function changeSourceImg(currentSource, newSource){
    let img = document.querySelector(`img[src="${currentSource}"]`)
    img.setAttribute('src', newSource)
}