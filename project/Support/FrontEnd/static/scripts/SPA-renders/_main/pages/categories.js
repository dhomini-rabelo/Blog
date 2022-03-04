export let categoriesSPA = {
    group: 'main',
    individualStyles: [
        '/static/styles/apps/categories/list_categories.css',
    ],
    content: 'categories',
    individualScripts: [
        ['/static/scripts/SPA-renders/_main_children/renderSubcategories.js', true]
    ]
}