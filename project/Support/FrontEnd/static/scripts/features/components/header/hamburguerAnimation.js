let hamburguer = document.querySelector('.hamburguer')

hamburguer.addEventListener('click', animateHamburguer)



function animateHamburguer(){
    let subMenu = document.querySelector('.sub-menu')
    hamburguer.classList.toggle('open')
    
    if (hamburguer.classList.contains('open')){
        subMenu.style.display = 'flex'
    }else{
        subMenu.style.display = 'none'
    }
}