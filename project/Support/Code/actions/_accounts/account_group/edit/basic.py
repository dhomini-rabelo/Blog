def save_user_basic_and_update_user_save(request):
    user = request.user
    name: str = request.POST.get('name')
    new_file = request.FILES.get('photo')
    if new_file:
        user.photo = new_file
    user.name = name.title()
    user.save()
    request.session['user_save']['name'] = name.title()
    request.session['user_save']['photo_path'] = user.photo.url
    request.session.save()