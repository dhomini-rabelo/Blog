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
        'posts': construct_posts_page(),
        'categories': construct_categories_page(),
        'authors': construct_authors_page(),
    }
    
    return main_spa
    