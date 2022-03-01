from celery import shared_task
from ..models import User
from posts.models import Post
from suggestions.models import SubCategorySuggestion, CategorySuggestion


def get_posts_list_html(posts):
    html = ''
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
    
    return html



def get_suggestions_list_html(suggestions):
    html = ''
    
    for suggestion in suggestions:
        match suggestion.state:
            case 'invalid' | 'reject':
                html += f"""
    <div class="suggestion-block center-c reject">
        <div class="suggestion-block-top sb-x">
            <span class="suggestion-name">{suggestion.name}</span>
            <div class="suggestion-status-color"><img src="/media/assets/account_group/suggestions/close.png" alt="" class="suggestion-img"></div>
        </div>
        <div class="suggestion-block-bottom sb-x">
            <span>Status</span>
            <span>Recusado</span>
        </div>
    </div>
                """
            case 'loading':
                html += f"""
    <div class="suggestion-block center-c loading">
        <div class="suggestion-block-top sb-x">
            <span class="suggestion-name">{suggestion.name}</span>
            <div class="suggestion-status-color"><img src="/media/assets/account_group/suggestions/time.png" alt="" class="suggestion-img"></div>
        </div>
        <div class="suggestion-block-bottom sb-x">
            <span>Status</span>
            <span>Em andamento</span>
        </div>
    </div>
                """
            case 'accept':
                html += f"""
    <div class="suggestion-block center-c accept">
        <div class="suggestion-block-top sb-x">
            <span class="suggestion-name">{suggestion.name}</span>
            <div class="suggestion-status-color"><img src="/media/assets/account_group/suggestions/check.png" alt="" class="suggestion-img"></div>
        </div>
        <div class="suggestion-block-bottom sb-x">
            <span>Status</span>
            <span>Aceito</span>
        </div>
    </div>                 
                """
    
    return html



@shared_task(name='USPGT_update_my_posts_list')
def update_posts_list(email: str, published: bool):
    user = User.objects.get(email=email)
    my_posts = Post.objects.filter(user__email=email).exclude(published=published).select_related('category')
    process = 'posts_list' if published else 'drafts_list'

    html = get_posts_list_html(my_posts)
    new_my_static_pages = user.my_static_pages.copy()
    new_my_static_pages['post'][process] = html
    
    user.my_static_pages = new_my_static_pages
    user.save()
    
    return {f'update_{process}': email}



@shared_task(name='USPGT_update_my_suggestions_list')
def update_suggestions(email:str, suggestion_type:str):
    user = User.objects.get(email=email)

    match suggestion_type:
        case 'categories':
            suggestions = CategorySuggestion.objects.filter(user__email=email)
        case 'subcategories':
            suggestions = SubCategorySuggestion.objects.filter(user__email=email)
        case _:
            raise ValueError('Invalid suggestion type')
        
    html = get_suggestions_list_html(suggestions)
    new_my_static_pages = user.my_static_pages.copy()
    new_my_static_pages['suggestions'][suggestion_type] = html
    
    user.my_static_pages = new_my_static_pages
    user.save()
    
    return {f'update_{suggestion_type}': email}
    