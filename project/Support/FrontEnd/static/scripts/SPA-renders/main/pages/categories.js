import { baseHeader } from "./support/constants.js"

export let categoriesSPA = {
    newHead: `${baseHeader.replace('{% block links %}', '<link rel="stylesheet" href="/static/styles/apps/categories/list_categories.css">')}`,
    newContent: `
    <div class="page-container flex-pass">
    <h1 class="page-title">Categorias</h1>
    <div class="main-container w-sb-x">
        <a href="/" class="box">
            <div class="box-body">
                <img src="/media/assets/posts/brasil.jpg" alt="post-img" class="box-img">
                <h2 class="box-title">Tecnologia</h2>
            </div>
        </a>
        
    </div>
</div>
    `,
    newScripts: []
}