from PIL import Image
from pathlib import Path
import io
from io import BytesIO



def resize(image_field):
    image_file = BytesIO(image_field.file.read())
    image = Image.open(image_file)
    image.thumbnail((30, 30), Image.ANTIALIAS)
    image_file = BytesIO()
    image.save(image_file, 'jpeg', optimized=True, quality=75)
    image_field.file = image_file
    image_field.image = image
    return image_field

