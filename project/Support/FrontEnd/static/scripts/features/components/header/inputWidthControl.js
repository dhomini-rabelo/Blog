let headerForm = document.querySelector('.search form')


headerForm.addEventListener('submit', controlInputWidth)


function controlInputWidth(event){
    let search = document.querySelector('.search')
    let input = document.querySelector('.search form input')
    let logoImg = document.querySelector('#dracula-logo')
    let logoTitle = document.querySelector('.logo-title')
    let header = document.querySelector('.header-pc')
    let ulNav = document.querySelector('ul.nav-x')
    
    
    
    if (input.value === '') {
        search.classList.toggle('search-input-mobile')
        
        if (search.classList.contains('search-input-mobile')){
            logoImg.classList.add('invisible')
            logoTitle.classList.add('invisible')

            header.classList.add('search-control')
            ulNav.classList.add('search-control')
        }else{
            logoImg.classList.remove('invisible')
            logoTitle.classList.remove('invisible')

            header.classList.remove('search-control')
            ulNav.classList.remove('search-control')
        }
        
        event.preventDefault()
    }
}


