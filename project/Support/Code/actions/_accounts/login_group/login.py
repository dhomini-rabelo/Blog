from pathlib import Path
from random import randint
from rest_framework_simplejwt.tokens import RefreshToken

def get_aleatory_profile_photo():
    path = 'C:/Users/G-fire/OneDrive/Documentos/GITHUB/DJANGO/Blog-Django-with-CBV/project/Support/FrontEnd/media/users/default'
    current_path = Path(path)
    archives = []
    for archive in current_path.iterdir():
        archives.append(archive.name)
    archives_quantity = len(archives)
    drawn_position = randint(0, archives_quantity-1)
    chosen_file = archives[drawn_position]
    return f'users/default/{chosen_file}'
    


def get_token_for_user(request):
    refresh = RefreshToken.for_user(request.user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }