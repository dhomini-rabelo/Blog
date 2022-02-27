from posts.models import Post
from categories.models import Category
from accounts.models import User


def construct_posts_page():
    html = '<div class="page-container flex-pass"><h1 class="page-title">Últimos posts</h1><div class="main-container">'
    posts = Post.objects.all().select_related('category')

    for post in posts:
        html += f"""
<a href="/" class="box">
    <div class="box-body center-c">
        <img src="{post.img.url}" alt="post-img" class="box-img">
        <h2 class="post-title">{post.title}</h2>
        <p class="box-description">{post.text}</p>
        <div class="box-info sb-x">
            <span class="post-category">{post.category.name}</span>
            <span class="post-date">{post.date}</span>
        </div>
    </div>
</a>
        """
    
    html += '</div></div>'
        
    return html


def construct_categories_page():
    html = '<div class="page-container flex-pass"><h1 class="page-title">Categorias</h1><div class="main-container-f w-sb-x">'
    categories = Category.objects.all()

    for category in categories:
        html += f"""
        <a href="/" class="box">
            <div class="box-body center-c">
                <img src="{category.img.url}" alt="post-img" class="box-img">
                <h2 class="box-title">{category.name}</h2>
            </div>
        </a>
        """
        
    html += '</div></div>'
        
    return html


def construct_authors_page():
    html = '<div class="page-container flex-pass"><h1 class="page-title">Autores</h1><div class="main-container-f w-sb-x">'
    authors = User.objects.all()

    for author in authors:
        html += f"""
        <a href="/" class="box">
            <div class="box-body center-c">
                <img src="{author.photo.url}" alt="post-img" class="box-img">
                <h2 class="box-title">{author.name}</h2>
            </div>
        </a>
        """
    
    html += '</div></div>'
        
    return html


def get_main_spa():
    main_spa = {
        
        'posts': {
            'html': construct_posts_page(),
            'update': False,
        },
        
        'categories': {
            'html': construct_categories_page(),
            'update': False,
        },
        
        'authors': {
            'html': construct_authors_page(),
            'update': False,
        },

    }
    return main_spa


def construct_page(local):
    match local:
        case 'posts':
            return construct_posts_page()
        case 'categories':
            return construct_categories_page()
        case 'authors':
            return construct_authors_page()



def update_main_spa(current_main: dict):
    main_spa = dict()
    updated_obj = {}
    updated = False

    
    for page, page_data in current_main.items():
        if page_data['update']:
            main_spa[page] = {
                'html': construct_page(page),
                'update': False,
            }
            updated_obj[page] = True
            updated = True
        else:
            main_spa[page] = page_data.copy()
            updated_obj[page] = False

    return {'spa': main_spa, 'report': updated_obj, 'updated': updated}
