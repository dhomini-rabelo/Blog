import {changeSourceImg} from './../../core/utils.js'

export function focusInFooter(){
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

    let ci = '/media/assets/posts/mobile-footer' // current image source
    changeSourceImg(`${ci}/${sourceImg}.png`, `${ci}/${sourceImg}-yellow.png`)
}


export function loseFocusInFooter() {
    let mobileFooterImgs = document.querySelectorAll('.navigation-img')

    mobileFooterImgs.forEach((img) => {

        if (img.src.slice(-11) === '-yellow.png') {
            let src = img.getAttribute('src')
            let oldSource = src.slice(0)
            let newSource = src.replace('-yellow.png', '.png')
            changeSourceImg(oldSource, newSource)
        }

    })

}