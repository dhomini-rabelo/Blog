from PIL import Image
from pathlib import Path
import io
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

def filter_name(name: str) -> str:
    bar = '\*'[0]
    name = name.replace('/', '').replace(bar, '')
    if '.' not in name:
        return f'{name}.png'
    elif name.endswith('.jpg'):
        return name.replace('jpg', 'jpeg')
    else:
        return name



def resize(image_field: InMemoryUploadedFile, image_name: str, max_width: int = 550):
    """
    max_width variable use px as metric
    """
    name = filter_name(image_name)
    image_extension = image_name.split('.')[-1]
    image_file = BytesIO(image_field.file.read())
    image = Image.open(image_file)
    width, height = image.size

    if width > max_width:
        image.thumbnail((max_width + 300, max_width), Image.ANTIALIAS)
        image_file = BytesIO()
        image.save(image_file, image_extension, optimized=True, quality=75)
        image_field.file = image_file
        image_field.image = image

    return image_field

