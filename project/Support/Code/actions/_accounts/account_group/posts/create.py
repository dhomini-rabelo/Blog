from Support.Code.Fast.models.cards import get_posts_list_html
from Support.Code.actions.Support.forms.utils import get_image
from Support.Code.actions.Support.utils.main import if_none
from Support.Code.actions._accounts.account_group.posts.support.create import generate_post_code
from categories.models import Category, SubCategory
from django.core.cache import cache
from posts.models import Post
from accounts.models import User
from django.utils.html import format_html
from .index import resize
from django.core.files.uploadedfile import UploadedFile




def create_draft_post(request, fields: dict):
    img = get_image(request, User.objects.get(username='default').photo)
    name = img.name if '.' in img.name else 'png'
    img = resize(img, img.name, 500)
    img.seek(0)
    post = Post.objects.create(
        title=fields['title'],
        description=fields['description'],
        text=if_none(request.POST.get('text'), ''),
        img=img,
        category=Category.objects.get(slug=fields['category']),
        author=request.user,
        code=generate_post_code(),
        published=False,
    )

    for subcategory in SubCategory.objects.filter(category__slug=fields['category'], slug__in=request.POST.getlist('subcategory')):
        post.sub_categories.add(subcategory)

    post.save()
    html = get_posts_list_html([post], True)
    update_posts_my_static_pages(request, html, 'drafts_list')

    return {
        'new_draft_post_url': f'/minha-conta/post/editar/{post.code}',
    }



def get_data_for_post_form(current_form):
    data = cache.get('context')
    return [
        data['categories'],
        data['subcategories'],
        current_form
    ]



def update_posts_my_static_pages(request, html, list_):
    request.session['user_save']['posts'][list_] += format_html(html)
    request.session.save()
    base = request.user.my_static_pages.copy()
    base['posts'][list_] += html
    request.user.my_static_pages = base
    request.user.save()