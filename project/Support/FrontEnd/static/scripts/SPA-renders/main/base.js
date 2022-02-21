import { addStyles, changeUrl, removeStyles, render } from '../core.js'
import { startAnimation, endAnimation } from '../../features/components/main/loadAnimation.js'
import { focusInFooter, loseFocusInFooter } from '../../features/components/footer/focus.js'


import { postsSPA } from './pages/posts.js'
import { categoriesSPA } from './pages/categories.js'
import { authorsSPA } from './pages/authors.js'



export function renderSPA(destiny) {

    let title = 'CODE PORTAL'
    let renderObj
    let newUrl

    switch (destiny){
        case 'posts':
            newUrl = '/'
            renderObj = postsSPA
            break
        case 'categories':
            newUrl = '/categorias/'
            renderObj = categoriesSPA
            break
        case 'authors':
            newUrl = '/autores/'
            renderObj = authorsSPA
            break
        case _:
            return
    }

    changeUrl(title, newUrl)

    startAnimation()

    render('.main', renderObj)

    loseFocusInFooter()
    
    focusInFooter()
    
    endAnimation()

}