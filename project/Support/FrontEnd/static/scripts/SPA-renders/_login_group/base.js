import { changeUrl, render } from './../core/main.js'
import { removeStyles, addStyles } from './../core/styles.js'
import { startAnimation, endAnimation } from '../../features/components/main/loadAnimation.js'
import { loginSPA } from './pages/login.js'
import { registerSPA } from './pages/register.js'



document.querySelector('.link-login-group').addEventListener('click', renderSPA)




function renderSPA(e) {
    e.preventDefault()

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
        case 'register':
            newUrl = '/cadastro/'
            renderObj = registerSPA
            title = 'CADASTRO'
            break
        default:
            throw new Error('Destiny not found')
    }

    changeUrl(title, newUrl)

    removeStyles([
        '/static/styles/features/colors/la1-2.css',
    ])

    addStyles('.style-animation', [
        '/static/styles/features/colors/la1-1.css',
    ])
    
    startAnimation()

    document.querySelector('form').setAttribute('for', newUrl)

    render('#form', renderObj, false)

    setTimeout(endAnimation, 200)

    document.querySelector('.link-login-group').removeEventListener('click', renderSPA)

    document.querySelector('.link-login-group').addEventListener('click', renderSPA)
}



window.addEventListener('popstate', function() {
    let lastUrl = localStorage.getItem('back')
    if(lastUrl){
        window.location.pathname = lastUrl
    }
})