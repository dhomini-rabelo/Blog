import { startAnimation, endAnimation } from '../../features/components/main/loadAnimation.js'
import { changeUrl } from './../core/main.js'
import { addStyles, removeStyles } from './../core/styles.js'
import { fetchGet } from './../../features/core/api.js'
import { renderPosts } from './support/render.js'



export async function renderPostsSubcategory(e){
    e.preventDefault()
    startAnimation()
    let box = e.currentTarget
    changeUrl('CODE PORTAL', `/categorias/subcategorias/${box.getAttribute('slug')}`)

    let url = `${window.location.origin}/api/posts-list/subcategory/${box.getAttribute('slug')}`
    let posts = await fetchGet(url, {})
    let container = document.querySelector('.main')
    let html = `<div class="page-container flex-pass"><h1 class="page-title">${box.querySelector('.box-title').innerHTML}</h1><div class="main-container">`


    html += renderPosts(posts)

    html += '</div></div>'
    container.innerHTML = html

    removeStyles(['/static/styles/apps/categories/list_categories.css'])
    addStyles('.styles-individual', ['/static/styles/apps/posts/index.css'])

    setTimeout(endAnimation, 200)
}