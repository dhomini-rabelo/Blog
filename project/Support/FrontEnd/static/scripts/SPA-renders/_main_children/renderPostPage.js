import { startAnimation, endAnimation } from '../../features/components/main/loadAnimation.js'
import { changeUrl } from '../core/main.js'
import { addStyles, removeStyles } from './../core/styles.js'
import { fetchGet } from '../../features/core/api.js'

document.querySelector('#box-post').addEventListener('click', renderPostPage)


export async function renderPostPage(e){
    e.preventDefault()
    startAnimation()
    let box = e.currentTarget
    changeUrl('CODE PORTAL', `/posts/post/${box.getAttribute('slug')}`)
    let url = `${window.location.origin}/api/get-post-for-main-spa/${box.getAttribute('slug')}`

    let post = await fetchGet(url, {})
    let container = document.querySelector('.main')
    
    let html = `
    <div class="page-container flex-pass">
        <div id="post" class="flex-pass">
        <h1 class="post-title">${box.querySelector('.post-title').innerHTML}</h1>
        <div class="center-c post-img">
            <img src="${post.img}" alt="post-img">
        </div>
        <p class="post-body">${post.text}</p>
        </div>
    </div>
    `    
    
    container.innerHTML = html

    removeStyles(['/static/styles/apps/posts/index.css'])
    addStyles('.styles-individual', ['/static/styles/apps/posts/post.css'])

    setTimeout(endAnimation, 200)
}