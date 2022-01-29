document.querySelector('.hamburguer-in-page-container').addEventListener('click', showMenu)
document.querySelector('.hamburguer-mobile-menu').addEventListener('click', showMenu)

function showMenu() {
    let pageContainer = document.querySelector('.page-container')
    let mobileMenu = document.querySelector('.account-group-menu')
    mobileMenu.classList.toggle('invisible')
    pageContainer.classList.toggle('invisible')
}
