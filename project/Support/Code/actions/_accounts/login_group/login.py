from pathlib import Path
from random import randint
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

def get_token_for_user(request):
    refresh = RefreshToken.for_user(request.user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }