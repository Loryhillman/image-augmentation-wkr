from PIL import Image

def flip_image(image, mode='horizontal'):
    """
    Отражает изображение по горизонтали или вертикали.
    
    :param image: PIL.Image
    :param mode: 'horizontal' или 'vertical' (или случайный выбор)
    :return: PIL.Image
    """
    if mode == 'horizontal':
        return image.transpose(Image.FLIP_LEFT_RIGHT)
    elif mode == 'vertical':
        return image.transpose(Image.FLIP_TOP_BOTTOM)
    else:
        raise ValueError("mode должен быть 'horizontal' или 'vertical'")