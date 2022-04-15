from .main import show_date


def get_posts_list_html(posts, edit_link=False):
    html = ''
    for post in posts:
        url = f'/posts/post/{post.code}' if not edit_link else f'/minha-conta/post/editar/{post.code}'
        html += f"""
    <a href="{url}" class="box" slug="{post.code}" id="box-post">
        <div class="box-body center-c">
            <img src="{post.img.url}" alt="post-img" class="box-img">
            <h2 class="post-title">{post.title}</h2>
            <p class="box-description">{post.description}</p>
            <div class="box-info sb-x">
                <span class="post-category">{post.category.name}</span>
                <span class="post-date">{show_date(post.created)}</span>
            </div>
        </div>
    </a>
    """
    
    return html



def get_categories_list_html(categories, is_subcategory=False):
    box_id = 'box-subcategory' if is_subcategory else 'box-category'
    html = ''
    for category in categories:
        html += f"""
        <a href="{category.get_path()}" class="box" slug="{category.slug}" id="{box_id}">
            <div class="box-body center-c">
                <img src="{category.img.url}" alt="post-img" class="box-img">
                <h2 class="box-title">{category.name}</h2>
            </div>
        </a>
    """
    
    return html



def get_authors_list_html(authors):
    html = ''
    
    for author in authors:
        html += f"""
        <a href="/autores/{author.slug}" class="box" slug="{author.slug}" id="box-author">
            <div class="box-body center-c">
                <img src="{author.my_static_pages['data']['photo_url']}" alt="post-img" class="box-img">
                <h2 class="box-title">{author.name}</h2>
            </div>
        </a>
        """
    
    return html


def get_suggestions_list_html(suggestions):
    html = ''
    
    for suggestion in suggestions:
        html+= get_suggestion_html(suggestion.name, suggestion.state)
    
    return html



def get_suggestion_html(suggestion, state):
    match state:
        case 'invalid':
            status_text = 'Inválido'
            img = 'close'
        case 'reject':
            status_text = 'Recusado'
            img = 'close'
        case 'loading':
            status_text = 'Em andamento'
            img = 'time'
        case 'accept':
            status_text = 'Aceito'
            img = 'check'
                
    suggestion_state = state if state != 'invalid' else 'reject'
            
    html = f"""
<div class="suggestion-block center-c {suggestion_state}">
    <div class="suggestion-block-top sb-x">
        <span class="suggestion-name">{suggestion}</span>
        <div class="suggestion-status-color"><img src="/static/media/assets/account_group/suggestions/{img}.png" alt="" class="suggestion-img"></div>
    </div>
    <div class="suggestion-block-bottom sb-x">
        <span>Status</span>
        <span>{status_text}</span>
    </div>
</div>
    """
    
    return html