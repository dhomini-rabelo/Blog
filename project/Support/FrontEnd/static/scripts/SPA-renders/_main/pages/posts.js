export let postsSPA = {
    group: 'main',
    individualStyles: [
            '/static/styles/apps/posts/index.css',
    ],
    content: 'posts',
    individualScripts: [
        ['/static/scripts/SPA-renders/_main_children/renderPostPage.js', true]
    ]
}