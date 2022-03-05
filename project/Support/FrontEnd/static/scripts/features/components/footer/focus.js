import {changeSourceImg} from './../../core/utils.js'

export function focusInFooter(){
    let urlRest = window.location.pathname
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
    styleInFooter(urlRest.slice(0, endPosition))
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

    noStyleInFooter()
}

function noStyleInFooter() {
    let mobileNavigations = document.querySelectorAll('.navigation')
    mobileNavigations.forEach((nav) => {
        nav.setAttribute('style', '')
        nav.querySelector('.mobile-navigation-text').setAttribute('style', '')
    })
}


function styleInFooter(focusLocal) {
    let st = 'border-top: 0.2px solid #ffc746;'
    let sr = 'border-right: 0.5px solid #ffc746;'
    let address = {
        '/': '#posts-link',
        '/posts/': '#posts-link',
        '/categorias/': '#categories-link',
        '/autores/': '#authors-link',
        '/minha-conta/': '#account-link',
    }
    let actions = {
        '/': `${st} ${sr}`,
        '/posts/': `${st} ${sr}`,
        '/categorias/': {
            '/posts/': sr,
            '/categorias/': `${st} ${sr}`,
        },
        '/autores/': {
            '/categorias/': sr,
            '/autores/': `${st} ${sr}`,
        },
        '/minha-conta/': {
            '/minha-conta/': st,
            '/autores/': sr,
        },
    }
    let action = actions[focusLocal]
    let currentWeFooter = document.querySelector(address[focusLocal])
    if (typeof action === 'string'){
        currentWeFooter.setAttribute('style', action)
    }else{
        for (let key of Object.keys(action)){
            let weFooter = document.querySelector(address[key])
            weFooter.setAttribute('style', action[key])
        }
    }    
    currentWeFooter.querySelector('.mobile-navigation-text').style.color = '#ffc746'
}