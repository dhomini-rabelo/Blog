from Support.Code.actions.Support.utils.main import if_none
from posts.models import Post
from categories.models import Category
from accounts.models import User
from ...models.cards import get_posts_list_html, get_authors_list_html, get_categories_list_html


def construct_posts_page(context):
    html = '<div class="page-container flex-pass"><h1 class="page-title">Últimos posts</h1><div class="main-container">'
    posts = if_none(context, Post.objects.all().select_related('category'))

    html += get_posts_list_html(posts)
    
    html += '</div></div>'
        
    return html


def construct_categories_page(context):
    html = '<div class="page-container flex-pass"><h1 class="page-title">Categorias</h1><div class="main-container-f w-se-x">'
    categories = if_none(context, Category.objects.all())

    html += get_categories_list_html(categories)
        
    html += '</div></div>'
        
    return html


def construct_authors_page(context):
    html = '<div class="page-container flex-pass"><h1 class="page-title">Autores</h1><div class="main-container-f w-se-x">'
    authors = if_none(context, User.objects.filter(posts__gte=1))

    html += get_authors_list_html(authors)
    
    html += '</div></div>'
        
    return html


def get_main_spa(context):
    main_spa = {
        
        'posts': construct_posts_page(context),
        'categories': construct_categories_page(context),
        'authors': construct_authors_page(context),

    }
    
    return main_spa


def construct_page(key):
    match key:
        case 'posts':
            return construct_posts_page(None)
        case 'categories':
            return construct_categories_page(None)
        case 'authors':
            return construct_authors_page(None)



def update_main_spa(current_main_spa: dict, updated_obj: dict):
    new_main_spa = dict()
    updated = False
    report = {}
    
    for key in current_main_spa.keys():
        if updated_obj[key]:
            new_main_spa[key] = construct_page(key)
            updated = True
            report[key] = True
        else:
            report[key] = False



    return {'spa': {**current_main_spa, **new_main_spa}, 'report': report, 'updated': updated}
