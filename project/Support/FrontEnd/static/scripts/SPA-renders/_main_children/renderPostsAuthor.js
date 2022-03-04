import { startAnimation, endAnimation } from '../../features/components/main/loadAnimation.js'
import { changeUrl } from '../core/main.js'
import { addStyles, removeStyles } from './../core/styles.js'
import { fetchGet } from '../../features/core/api.js'
import { renderPosts } from './support/render.js'
import { active as activeRenderPostPage } from './renderPostPage.js'


active()

document.querySelector('.mobile-footer .navigation#authors-link').addEventListener('click', active)
document.querySelector('.pc-link-navigation[destiny="authors"]').addEventListener('click', active)

function active() {
    let authorsBox = document.querySelectorAll('#box-author')
    authorsBox.forEach((box) => {
        box.removeEventListener('click', renderPostsAuthor)
        box.addEventListener('click', renderPostsAuthor)
    })
}



export async function renderPostsAuthor(e){
    e.preventDefault()
    startAnimation()
    let box = e.currentTarget
    changeUrl('CODE PORTAL', `/autores/${box.getAttribute('slug')}`)

    let url = `${window.location.origin}/api/posts-list/author/${box.getAttribute('slug')}`
    let posts = await fetchGet(url, {})
    let container = document.querySelector('.main')
    let html = `<div class="page-container flex-pass"><h1 class="page-title">${box.querySelector('.box-title').innerHTML}</h1><div class="main-container">`


    html += renderPosts(posts)

    html += '</div></div>'
    container.innerHTML = html

    removeStyles(['/static/styles/apps/authors/list_authors.css'])
    addStyles('.styles-individual', ['/static/styles/apps/posts/index.css'])

    activeRenderPostPage()

    setTimeout(endAnimation, 350)
}