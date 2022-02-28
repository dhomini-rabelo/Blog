import json
from accounts.models import User


def construct_user_may_static_page(user):
    user_static_page = {
        
        'data': {
            'photo_url': user.photo.url,
            'name': user.name,
            'email': user.email,
        },

        'post': {
            'posts_list': '',
            'drafts_list': '',
        },
        
        'suggestions': {
            'categories': '',
            'subcategories': '',
        },

    }
    
    return json.loads(user_static_page)

