let mainListOptions = document.querySelectorAll('.main-list .menu-mobile-item')

mainListOptions.forEach((item) => {
    item.addEventListener('click', changeMenu)
})

function changeMenu(event) {
    let selectedOption = event.currentTarget

    let mainList = document.querySelector('.main-list')
    let newOptions = document.querySelector(`.${selectedOption.getAttribute('open')}`)
    
    mainList.classList.add('invisible')
    newOptions.classList.remove('invisible')
}