from Support.Code.actions.Support.utils.functions_dict import get_name
from django.utils.text import slugify


def save_user_basic_and_update_user_save(request):
    user = request.user
    name: str = request.POST.get('name')
    new_file = request.FILES.get('photo')
    if new_file:
        user.photo = new_file
    user.name = get_name(name)
    new_slug = slugify(name)
    if request.session['user_save']['data']['author']:
        new_slug = f'{new_slug}-{user.id}'
    user.slug = new_slug
    user.save()
    request.session['user_save']['data']['name'] = get_name(name)
    request.session['user_save']['data']['slug'] = new_slug
    request.session['user_save']['data']['photo_url'] = user.photo.url
    request.session.save()
    user.my_static_pages = {**user.my_static_pages, 'data': request.session['user_save']['data']}
    user.save()