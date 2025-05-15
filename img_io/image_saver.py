from PIL import Image
import os

def save_image(image, path):
    """Сохраняет изображение в формате PNG, если есть альфа-канал, иначе JPEG"""
    base, ext = os.path.splitext(path)
    

    new_path = base + '.png'


    if image.mode in ['RGBA', 'LA']:
        image = image.convert('RGBA')


    image.save(new_path, format='PNG')