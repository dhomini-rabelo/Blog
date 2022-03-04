import { startAnimation, endAnimation } from '../../features/components/main/loadAnimation.js'
import { changeUrl } from './../core/main.js'
import { renderPostsSubcategory } from './renderPostsSubcategory.js'
document.querySelector('#box-category').addEventListener('click', loadSubcategoriesList)


function loadSubcategoriesList(e) {
    e.preventDefault()
    startAnimation()
    
    let box = e.currentTarget
    changeUrl('CODE PORTAL', `/categorias/${box.getAttribute('slug')}/subcategorias/`)
    let container = document.querySelector('.main-container-f')
    let title = document.querySelector('.page-title')
    let html = ''
    
    let spaObj = JSON.parse(document.querySelector('#SPGT').value)
    let subcategoriesData = spaObj.main.subcategories
    
    let subcategoriesList = subcategoriesData[box.getAttribute('slug')]
    
    subcategoriesList.forEach((subcategory) => {
        html += `
        <a href="/categorias/subcategorias/${subcategory.slug}" class="box" slug="${subcategory.slug}" id="box-subcategory">
            <div class="box-body center-c">
                <img src="${subcategory.img}" alt="post-img" class="box-img">
                <h2 class="box-title">${subcategory.name}</h2>
            </div>
            </a>
            `
        })
    container.innerHTML = html
    title.innerHTML = box.querySelector('.box-title').innerHTML
    document.querySelector('#box-subcategory').removeEventListener('click', renderPostsSubcategory)
    document.querySelector('#box-subcategory').addEventListener('click', renderPostsSubcategory)
    setTimeout(endAnimation, 200)
}