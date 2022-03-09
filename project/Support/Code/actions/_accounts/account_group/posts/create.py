from Support.Code.actions._accounts.account_group.posts.support.create import generate_post_code
from posts.models import Post



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
