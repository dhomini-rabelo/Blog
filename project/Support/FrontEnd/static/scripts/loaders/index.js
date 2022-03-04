import { focusInFooter } from '../features/components/footer/focus.js'
import { endAnimation } from '../features/components/main/loadAnimation.js'

document.addEventListener('DOMContentLoaded', useInitialScripts)

function useInitialScripts() {
    focusInFooter()
    setTimeout(endAnimation, 350)
}
window.addEventListener('popstate', function() {
    let lastUrl = localStorage.getItem('back')
    if(lastUrl){
        window.location.pathname = lastUrl
    }
})