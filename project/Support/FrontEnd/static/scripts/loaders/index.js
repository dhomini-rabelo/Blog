import { focusInFooter } from '../features/components/footer/focus.js'
import { endAnimation } from '../features/components/main/loadAnimation.js'

document.addEventListener('DOMContentLoaded', useInitialScripts)

function useInitialScripts() {
    focusInFooter()
    setTimeout(endAnimation, 100)
}