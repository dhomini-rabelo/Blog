from posts.models import Post
from categories.models import Category, SubCategory


def update_post(request, code, values, action=None):
    post = Post.objects.get(code=code)

    for attr in ['title', 'description', 'text']:
        setattr(post, attr, values[attr])

    img = request.FILES.get('img')
    if img is not None:
        post.img = img

    if post.category.slug == values.get('category'):
        post.category = Category.objects.get(slug=values.get('category'))

    current_subcategories = list(post.sub_categories.values_list('slug', flat=True))
    form_subcategories = values['subcategory']

    if current_subcategories != form_subcategories:
        post.sub_categories = [SubCategory.objects.get(slug=subcategory) for subcategory in values['subcategory']]

    if action in ['save-and-publish', 'save-and-unpublish']:
        state = True if action == 'save-and-publish' else False
        setattr(post, 'published', state)
        
    post.save()
