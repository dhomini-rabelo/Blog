let animationContent = document.querySelector('.load-animation')
let animationMainContent = document.querySelector('main')

export function endAnimation(){
    animationContent.classList.add('invisible')
    animationMainContent.classList.remove('invisible')
}

export function startAnimation() {
    animationContent.classList.remove('invisible')
    animationMainContent.classList.add('invisible')
}