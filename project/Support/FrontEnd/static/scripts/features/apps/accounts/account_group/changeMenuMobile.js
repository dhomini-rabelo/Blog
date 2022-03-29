let mainListOptions = document.querySelectorAll('.main-list .menu-mobile-item')

mainListOptions.forEach((item) => {
    item.addEventListener('click', changeMenu)
})

document.querySelector('.fa-angle-left').addEventListener('click', backMenu)



let currentOpen = ''


function changeMenu(event) {
    let selectedOption = event.currentTarget

    let newOptions = document.querySelector(`.${selectedOption.getAttribute('open')}`)
    let mainList = document.querySelector('.main-list')

    currentOpen = selectedOption.getAttribute('open')
    
    if (currentOpen !== 'close'){
        controlBackButton('add')
        mainList.classList.add('invisible')
        newOptions.classList.remove('invisible')
    }
}



function backMenu() {
    if (currentOpen === 'close'){ return }
    let currentOptions = document.querySelector(`.${currentOpen}`)
    let mainList = document.querySelector('.main-list')

    mainList.classList.remove('invisible')
    currentOptions.classList.add('invisible')

    controlBackButton('remove')
}



export function controlBackButton(action) {
    let menu = document.querySelector('.close-account-menu')
    let backButton = document.querySelector('.fa-angle-left')

    switch (action){
        case 'add':
            menu.classList.remove('end-r')
            menu.classList.add('sb-x')
            backButton.classList.remove('invisible')
            break
        case 'remove':
            backButton.classList.add('invisible')
            menu.classList.remove('sb-x')
            menu.classList.add('end-r')
            break
    }

}




