import {changeSourceImg} from './../../core/utils.js'

document.addEventListener('DOMContentLoaded', focusInFooter)



function focusInFooter(){
    let urlRest = window.location.pathname
    let baseSource = '/media/assets/posts/mobile-footer'
    let sourceImg
    let endPosition = urlRest.indexOf('/', 1) === -1 ? 1 : urlRest.indexOf('/', 1) + 1

    switch (urlRest.slice(0, endPosition)){
        case '/':
            sourceImg = 'post'
            break
        case '/posts/':
            sourceImg = 'post'
            break
        case '/categorias/':
            sourceImg = 'category'
            break
        case '/autores/':
            sourceImg = 'author'
            break
        case '/minha-conta/':
            sourceImg = 'user'
            break
    }


    let oldSource = `${baseSource}/${sourceImg}.png`
    let newSource = `${baseSource}/${sourceImg}-yellow.png`

    changeSourceImg(oldSource, newSource)
}


