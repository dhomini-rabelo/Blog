from .main import show_date


def get_posts_list_html(posts):
    html = ''
    for post in posts:
        html += f"""
    <a href="/posts/post/{post.code}" class="box" slug="{post.code}" id="box-post">
        <div class="box-body center-c">
            <img src="{post.img.url}" alt="post-img" class="box-img">
            <h2 class="post-title">{post.title}</h2>
            <p class="box-description">{post.description}</p>
            <div class="box-info sb-x">
                <span class="post-category">{post.category.name}</span>
                <span class="post-date">{show_date(post.date)}</span>
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
                <img src="{author.photo.url}" alt="post-img" class="box-img">
                <h2 class="box-title">{author.name}</h2>
            </div>
        </a>
        """
    
    return html


def get_suggestions_list_html(suggestions):
    html = ''
    
    for suggestion in suggestions:
        
        match suggestion.state:
            case 'invalid' | 'reject':
                status_text = 'Recusado'
            case 'loading':
                status_text = 'Em andamento'
            case 'accept':
                status_text = 'Aceito'
                
        suggestion_state = suggestion.state if suggestion.state != 'invalid' else 'reject'
                
        html += f"""
    <div class="suggestion-block center-c {suggestion_state}">
        <div class="suggestion-block-top sb-x">
            <span class="suggestion-name">{suggestion.name}</span>
            <div class="suggestion-status-color"><img src="/media/assets/account_group/suggestions/close.png" alt="" class="suggestion-img"></div>
        </div>
        <div class="suggestion-block-bottom sb-x">
            <span>Status</span>
            <span>{status_text}</span>
        </div>
    </div>
        """
    
    return html