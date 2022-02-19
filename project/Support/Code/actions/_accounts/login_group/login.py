from pathlib import Path
from random import randint

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
    