from accounts.models import User


def update_users_static_pages():
    users = User.objects.all()

    for user in users:
        pass


def construct_my_static(user):
    user_static_page = {
        
        'data': {
            'photo_url': user.photo.url,
            'name': user.name,
            'email': user.email,
        },

        'post': {
            'posts_list': '',
            'drafts_list': '',
        }

    }