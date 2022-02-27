import { changeUrl, render } from './../core/main.js'
import { removeStyles, addStyles } from './../core/styles.js'
import { startAnimation, endAnimation } from '../../features/components/main/loadAnimation.js'
import { loginSPA } from './pages/login.js'
import { registerSPA } from './pages/register.js'



document.querySelector('.link-login-group').addEventListener('click', renderSPA)




function renderSPA(e) {

    let destiny = e.currentTarget.getAttribute('destiny')
    
    let title
    let renderObj
    let newUrl

    
    switch (destiny){
        case 'login':
            newUrl = '/login/'
            renderObj = loginSPA
            title = 'LOGIN'
            break
        case 'cadastro':
            newUrl = '/cadastro/'
            renderObj = registerSPA
            title = 'CADASTRO'
            break
        case _:
            throw new Error('Destiny not found')
    }

    changeUrl(title, newUrl)

    removeStyles([
        '/static/styles/features/colors/la1-2.css',
    ])

    addStyles([
        '/static/styles/features/colors/la1-1.css',
    ])
    
    startAnimation()

    render('#form', renderObj)

    controlEvents(destiny, renderObj)

    endAnimation()

    document.querySelector('.link-login-group').removeEventListener('click', renderSPA)

    document.querySelector('.link-login-group').addEventListener('click', renderSPA)
}