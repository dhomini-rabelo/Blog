from Support.Code.Fast.models.cards import get_posts_list_html
from Support.Code.actions.Support.forms.utils import get_image
from Support.Code.actions.Support.utils.main import if_none
from Support.Code.actions._accounts.account_group.posts.support.create import generate_post_code
from categories.models import Category, SubCategory
from django.core.cache import cache
from posts.models import Post


def create_draft_post(request, fields: dict):
    post = Post.objects.create(
        title=fields['title'],
        description=fields['description'],
        text=if_none(request.POST.get('text'), ''),
        img=get_image(request, 'posts/default/code.jpg'),
        category=Category.objects.get(slug=fields['category']),
        author=request.user,
        code=generate_post_code(),
        published=False,
    )

    for subcategory in SubCategory.objects.filter(category__slug=fields['category'], slug__in=request.POST.getlist('subcategory')):
        post.sub_categories.add(subcategory)

    post.save()
    request.session['user_save']['posts']['drafts_list'] += get_posts_list_html([post])
    request.session.save()
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