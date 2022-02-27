import { changeUrl, render } from './../core/main.js'
import { removeStyles } from './../core/styles.js'
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
                throw new Error('Destiny not found')
    }

    changeUrl(title, newUrl)

    removeStyles([
        '/static/styles/features/colors/la1-1.css',
        '/static/styles/features/colors/la1-2.css',
    ])
    
    startAnimation()

    render('.main', renderObj)

    loseFocusInFooter()
    
    focusInFooter()
    
    endAnimation()

}