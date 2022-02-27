import { changeUrl, render } from './../core/main.js'
import { removeStyles, addStyles } from './../core/styles.js'
import { startAnimation, endAnimation } from '../../features/components/main/loadAnimation.js'
import { loginSPA } from './pages/login.js'
import { registerSPA } from './pages/register.js'



document.querySelector('.link-login-group').addEventListener('click', renderSPA)




function renderSPA(e) {

    let title = 'CODE PORTAL'
    let renderObj
    let newUrl

    let destiny = e.currentTarget.getAttribute('destiny')

    switch (destiny){
        case 'login':
            newUrl = '/login/'
            renderObj = loginSPA
            break
        case 'cadastro':
            newUrl = '/cadastro/'
            renderObj = registerSPA
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