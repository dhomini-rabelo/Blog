import json
from random import randint
from accounts.models import User
from rest_framework_simplejwt.tokens import RefreshToken

def get_aleatory_profile_photo():
    archives = [
        'aviao.png',
        'bandeira.png',
        'bitcoin.png',
        'cha.png',
        'chuva.png',
        'computador.png',
        'controle.png',
        'coquetel.png',
        'euro.png',
        'floco-de-neve.png',
        'foguete.png',
        'foto.py',
        'globo-terrestre.png',
        'hamburger.png',
        'lua.png',
        'luva.png',
        'mao.png',
        'medalha-de-bronze.png',
        'medalha-de-ouro.png',
        'medalha-de-prata.png',
        'moon.png',
        'oculos-escuros.png',
        'pizza.png',
        'presente.png',
        'relampago.png',
        'rocketseat.png',
        'servidor.png',
        'simbolo-do-dolar.png',
        'sol.png',
        'ufo.png',
        'xicara-de-cafe.png',
    ]

    archives_quantity = len(archives)
    drawn_position = randint(0, archives_quantity-1)
    chosen_file = archives[drawn_position] 
    return f'users/default/{chosen_file}'
    
get_aleatory_profile_photo()


def get_token_for_user(email):
    user = User.objects.get(email=email)
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    

def construct_user_my_static_page(user):
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
    
    return user_static_page