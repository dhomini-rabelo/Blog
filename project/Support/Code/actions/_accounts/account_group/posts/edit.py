from Support.Code.Fast.models.cards import get_posts_list_html
from categories.models import Category, SubCategory
from posts.models import Post
from django.utils.html import format_html

def update_post(request, code, values, action=None):
    post = Post.objects.get(code=code)

    for attr in ['title', 'description', 'text']:
        setattr(post, attr, values[attr])

    img = request.FILES.get('img')
    if img is not None:
        post.img = img

    if post.category.slug != values.get('category'):
        post.category = Category.objects.get(slug=values.get('category'))

    current_subcategories = list(post.sub_categories.values_list('slug', flat=True))
    form_subcategories = values['subcategory']

    if current_subcategories != form_subcategories:
        post.sub_categories.set([SubCategory.objects.get(slug=subcategory) for subcategory in values['subcategory']])

    if action in ['save-and-publish', 'save-and-unpublish']:
        state = True if action == 'save-and-publish' else False
        setattr(post, 'published', state)
    post.save()
    update_post_list_my_static_user_pages(request)
        



def update_post_list_my_static_user_pages(request):
    user = request.user
    
    posts = user.posts.select_related('category')
    drafts_html = get_posts_list_html(posts.filter(published=False).distinct().order_by('created'), True)
    published_html = get_posts_list_html(posts.filter(published=True).distinct().order_by('created'), True)
    
    request.session['user_save']['posts']['drafts_list'] = format_html(drafts_html)
    request.session['user_save']['posts']['posts_list'] = format_html(published_html)
    request.session.save()

    request.user.my_static_pages = request.session['user_save'].copy()
    
    user.save()