let hamburguer = document.querySelector('.hamburguer')


hamburguer.addEventListener('click', animateHamburguer)




function animateHamburguer(){
    let subMenu = document.querySelector('.sub-menu')
    hamburguer.classList.toggle('open')
    
    if (hamburguer.classList.contains('open')){
        subMenu.setAttribute('class', 'sub-menu flex')
    }else{
        subMenu.setAttribute('class', 'sub-menu invisible')
    }
}
