def change_user_email(request, new_email):
    user = request.user
    user.email = new_email
    user.username = new_email
    user.save()