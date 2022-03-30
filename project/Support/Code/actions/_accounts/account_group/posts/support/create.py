from Support.Code.actions.Support.forms.validators import validate_unique
from posts.models import Post
from random import randint



def generate_post_code():
    draw_number = randint(10000, 2147483647)
    check = validate_unique(Post, 'code', draw_number)

    while check is False:
        draw_number = randint(10000, 2147483647)
        check = validate_unique(Post, 'code', draw_number)

    return draw_number

