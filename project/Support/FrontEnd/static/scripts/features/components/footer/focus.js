import {changeSourceImg} from './../../core/utils.js'

document.addEventListener('DOMContentLoaded', focusInFooter)



function focusInFooter(){
    let urlRest = window.location.pathname
    let baseSource = '/media/assets/posts/mobile-footer'
    let sourceImg

    switch (urlRest){
        case '/':
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


