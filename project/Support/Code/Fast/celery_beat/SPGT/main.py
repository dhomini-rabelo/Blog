from Support.Code.actions.Support.utils.main import if_none
from posts.models import Post
from categories.models import Category, SubCategory
from accounts.models import User
from ...models.cards import get_posts_list_html, get_authors_list_html, get_categories_list_html
from django.utils.html import format_html


def construct_posts_page(context):
    html = '<div class="page-container flex-pass"><h1 class="page-title">Últimos posts</h1><div class="main-container">'
    posts = if_none(context.get('posts'), Post.objects.filter(published=True).select_related('category'))

    html += get_posts_list_html(posts)
    
    html += '</div></div>'
        
    return format_html(html)


def construct_categories_page(context):
    html = '<div class="page-container flex-pass"><h1 class="page-title">Categorias</h1><div class="main-container-f w-se-x">'
    categories = if_none(context.get('categories'), Category.objects.all())

    html += get_categories_list_html(categories)
        
    html += '</div></div>'
        
    return format_html(html)


def construct_authors_page(context):
    html = '<div class="page-container flex-pass"><h1 class="page-title">Autores</h1><div class="main-container-f w-se-x">'
    authors = if_none(context.get('authors'), User.objects.filter(posts__gte=1))

    html += get_authors_list_html(authors)
    
    html += '</div></div>'
        
    return format_html(html)


def construct_subcategories_data(context):
    subcategories_data = {}
    context_categories = if_none(context.get('categories'), Category.objects.all())
    context_subcategories = if_none(context.get('subcategories'), SubCategory.objects.all())
    
    for category in context_categories:
        subcategories = context_subcategories.filter(category=category)
        subcategories_data[category.slug] = [{'name': subcategory.name, 'img': subcategory.img.url, 'slug': subcategory.slug} for subcategory in subcategories]
        
    return subcategories_data
        

def get_main_spa(context):
    main_spa = {
        
        'posts': construct_posts_page(context),
        'categories': construct_categories_page(context),
        'authors': construct_authors_page(context),
        'subcategories': construct_subcategories_data(context),
    }
    
    return main_spa


def construct_page(key, context):
    match key:
        case 'posts':
            return construct_posts_page(context)
        case 'categories':
            return construct_categories_page(context)
        case 'authors':
            return construct_authors_page(context)
        case 'subcategories':
            return construct_subcategories_data(context)



def update_main_spa(current_main_spa: dict, context: dict, updated_obj: dict):
    new_main_spa = dict()
    updated = False
    report = {}
    
    for key in current_main_spa.keys():
        if updated_obj[key]:
            new_main_spa[key] = construct_page(key, context)
            updated = True
            report[key] = True
        else:
            report[key] = False



    return {'spa': {**current_main_spa, **new_main_spa}, 'report': report, 'updated': updated}
