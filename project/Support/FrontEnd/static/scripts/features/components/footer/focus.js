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

    loseFocusInFooter()
    let img = document.querySelector(`img[src="${baseSource}/${sourceImg}.svg"]`)
    setTimeout(() => {img.setAttribute('style', 'background-color: #ffc746;')}, 100)
}


export function loseFocusInFooter() {
    let mobileFooterImgs = document.querySelectorAll('.navigation-img')

    setTimeout(() =>{
        mobileFooterImgs.forEach((img) => {
        img.setAttribute('style', 'background-color: #fff;')
        })
    }, 80)

}