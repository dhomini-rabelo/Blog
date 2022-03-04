export let authorsSPA = {
    group: 'main',
    individualStyles: [
        '/static/styles/apps/authors/list_authors.css',
    ],
    content: 'authors',
    individualScripts: [
        ['/static/scripts/SPA-renders/_main_children/renderPostsAuthor.js', true],
    ]
}