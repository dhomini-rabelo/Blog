from Support.Code.actions._accounts.account_group.posts.support.create import generate_post_code
from posts.models import Post
from categories.models import Category, SubCategory
from django.core.cache import cache



def create_draft_post(request, fields: dict):
    post = Post.models.create(
        **fields,
        author=request.user,
        code=generate_post_code(),
        published=False,
    )

    return {
        'new_draft_post_url': f'/minha-conta/post/editar/{post.code}',
    }



def get_data_for_post_form(current_form):
    data = cache.get_many(['categories', 'subcategories'])
    return [
        data['categories'],
        data['subcategories'],
        current_form
    ]