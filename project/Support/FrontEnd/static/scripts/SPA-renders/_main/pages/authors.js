import { baseHead } from "./support/constants.js"

export let authorsSPA = {
    newHead: {
        ...baseHead,
        individualStyles: [
            '/static/styles/apps/authors/list_authors.css',
        ]
    },
    newContent: `
    <div class="page-container flex-pass">
    <h1 class="page-title">Autores</h1>
    <div class="main-container-f w-sb-x">
        <a href="/" class="box">
            <div class="box-body center-c">
                <img src="/media/assets/posts/brasil.jpg" alt="post-img" class="box-img">
                <h2 class="box-title">Dhomini Rabelo</h2>
            </div>
        </a>
        
    </div>
</div>
    `,
    newScripts: []
}