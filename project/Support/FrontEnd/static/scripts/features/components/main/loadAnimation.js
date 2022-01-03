document.addEventListener('DOMContentLoaded', changeContent)


function changeContent(){
    let animationContent = document.querySelector('.load-animation')
    let mainContent = document.querySelector('main')

    animationContent.classList.add('invisible')
    mainContent.classList.remove('invisible')
}