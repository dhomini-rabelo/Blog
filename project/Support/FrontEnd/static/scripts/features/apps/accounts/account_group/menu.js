document.querySelector('.hamburguer-in-page-container').addEventListener('click', showMenu)
document.querySelector('.hamburguer-mobile-menu').addEventListener('click', closeMenu)

let pageContainer = document.querySelector('.page-container')
let mobileMenu = document.querySelector('.account-group-menu')

function showMenu() {
    mobileMenu.classList.toggle('invisible')
    pageContainer.classList.toggle('invisible')
}

function closeMenu() {
    let subMenus = document.querySelectorAll('.menu-mobile-list')
    let mainList = document.querySelector('.main-list')

    mobileMenu.classList.toggle('invisible')
    pageContainer.classList.toggle('invisible')

    subMenus.forEach((menu) => {
        menu.classList.add('invisible')
    })
    mainList.classList.remove('invisible')
}