import { fetchPost } from "../../core/api.js"

let searchForm = document.querySelector('#search-form')

searchForm.addEventListener('submit', renderSearch)
let searches = {}


async function renderSearch(e) {
    e.preventDefault()
    let container = document.querySelector('.page-container')
    let input = document.querySelector('#search_box')
    if (input.value === '') return

    if(!(input.value.toLowerCase() in searches)){

        let url = `${window.location.origin}/api/search`
        let response = await fetchPost(url, {
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                search: input.value
            })
        })
        searches[input.value.toLowerCase()] = response
    }

    let data = searches[input.value.toLowerCase()]
    let containerHtml = `<h1 class="page-title">Busca por "${input.value}"</h1>`
    data.posts.forEach((post, index, array) => {
        if (index === 0) {
            containerHtml += `<h2 class="page-title" style="font-size: 1.2rem;">Posts (${array.length})</h2><div class="main-container">`
        }
        containerHtml += renderBox(post, 'box-post')
        if (index === array.length-1) {containerHtml += '</div>'}
    })
    data.categories.forEach((category, index, array) => {
        if (index === 0) {
            containerHtml += `<h2 class="page-title" style="font-size: 1.2rem;">Categorias (${array.length})</h2><div class="main-container-f w-se-x">`
        }
        containerHtml += renderBox(category, 'box-category')
        if (index === array.length-1) {containerHtml += '</div>'}
    })
    data.subcategories.forEach((subcategory, index, array) => {
        if (index === 0) {
            containerHtml += `<h2 class="page-title" style="font-size: 1.2rem;">Subcategorias (${array.length})</h2><div class="main-container-f w-se-x">`
        }
        containerHtml += renderBox(subcategory, 'box-subcategory')
        if (index === array.length-1) {containerHtml += '</div>'}
    })
    data.authors.forEach((author, index, array) => {
        if (index === 0) {
            containerHtml += `<h2 class="page-title" style="font-size: 1.2rem;">Autores (${array.length})</h2><div class="main-container-f w-se-x">`
        }
        containerHtml += renderBox(author, 'box-author')
        if (index === array.length-1) {containerHtml += '</div>'}
    })
    container.innerHTML = containerHtml
}


function renderBox(obj, id) {
    return `
    <a href="${obj.url}" class="box" slug="none" id="${id}">
        <div class="box-body center-c">
            <img src="${obj.img}" alt="post-img" class="box-img">
            <h2 class="box-title">${obj.title}</h2>
        </div>
    </a>
    `
} 