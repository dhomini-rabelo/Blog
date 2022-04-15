import { renderPost } from "./../../../SPA-renders/_main_children/support/render.js"
import { fetchPost } from "./../../core/api.js"

let searchForm = document.querySelector('form[method="GET"]')

searchForm.addEventListener('submit', renderSearch)


let results = {}


async function renderSearch(e) {
    e.preventDefault()
    let container = document.querySelector('.page-container')
    let input = document.querySelector('#search_box')
    if (input.value === '') return


    if (!(input.value.toLowerCase() in results)) {
        let url = `${window.location.origin}/api/search`
        let response = await fetchPost(url, {
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                search: input.value
            })
        })
        
        let data = response
        let containerHtml = `<h1 class="page-title">Busca por "${input.value}"</h1>`

        let renderTypes = {
            posts: {
                boxContainer: 'main-container', 
                boxType: 'posts',
            },
            default: {
                boxContainer: 'main-container-f w-se-x', 
                boxType: 'default',
            }
        }

        let initialContainerData = containerHtml

        containerHtml += renderData(data.posts, {title: 'Posts', id: 'box-post'}, renderTypes.posts)
        containerHtml += renderData(data.categories, {title: 'Categorias', id: 'box-category'}, renderTypes.default)
        containerHtml += renderData(data.subcategories, {title: 'SubCategorias', id: 'box-subcategory'}, renderTypes.default)
        containerHtml += renderData(data.authors, {title: 'Autores', id: 'box-author'}, renderTypes.default)
        
        if (initialContainerData === containerHtml) {
            containerHtml += '<div style="margin-top: 2rem; text-align: center;"><span style="color: white;">nada foi encontrado</span></div>'
        }

        results[input.value.toLowerCase()] = containerHtml
    }
    
    container.innerHTML = results[input.value.toLowerCase()]
}

function renderData(data, mySettings, settings) {
    if (data.length === 0) return ''

    let html = ''
    html += getTitle(mySettings.title, data.length, settings.boxContainer)
    data.forEach((obj) => {
        html += renderBox(obj, mySettings.id, settings.boxType)
    })
    html += '</div>'
    return html
}

function getTitle(title, length, dataContainer) {
    return `<h2 class="page-title" style="font-size: 1.2rem;">${title} (${length})</h2><div class="${dataContainer}">`
}


function renderBox(obj, id, boxType) {
    switch(boxType){
        case 'default':
            return `
            <a href="${obj.url}" class="box" slug="none" id="${id}">
                <div class="box-body center-c">
                    <img src="${obj.img}" alt="post-img" class="box-img">
                    <h2 class="box-title">${obj.title}</h2>
                </div>
            </a>
            `
        case 'posts':
            return renderPost(obj)
    }
} 