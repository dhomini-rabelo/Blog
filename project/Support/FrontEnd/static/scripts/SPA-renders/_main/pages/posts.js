import { baseHead } from "./support/constants.js"

export let postsSPA = {
    newHead: {
        ...baseHead,
        individualStyles: [
            '/static/styles/apps/posts/index.css',
        ]
    },
    newContent: `
    <div class="page-container flex-pass">
    <h1 class="page-title">Últimos posts</h1>
    <div class="main-container">
        <a href="/" class="box">
            <div class="box-body center-c">
                <img src="/media/assets/posts/brasil.jpg" alt="post-img" class="box-img">
                <h2 class="post-title">5G no Brasil</h2>
                <p class="box-description">
                    Nova tecnologia será implantada em julho de 2022. As operadoras que venceram as disputas Lo, Lorem ipsum dolor sit amet, consectetur adipisicing elit. Molestiae ut dolores pariatur quaerat eius laudantium. Assumenda ipsum quisquam sequi eligendi, voluptatum suscipit tempora expedita consequatur reiciendis ex. Fuga, neque aspernatur.
                </p>
                <div class="box-info sb-x">
                    <span class="post-category">Tecnologia</span>
                    <span class="post-date">14/12</span>
                </div>
            </div>
        </a>
        
    </div>
</div>
    `,
    newScripts: []
}