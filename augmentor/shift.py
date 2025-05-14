from PIL import Image
import random

def shift_image(image, max_shift=0.1):
    """
    Сдвиг изображения на случайное расстояние по горизонтали и вертикали.

    :param image: изображение для сдвига
    :param max_shift: максимальный процент сдвига от размера изображения
    :return: сдвинутое изображение
    """
    width, height = image.size
    max_shift_x = int(width * max_shift)
    max_shift_y = int(height * max_shift)

    shift_x = random.randint(-max_shift_x, max_shift_x)
    shift_y = random.randint(-max_shift_y, max_shift_y)

    shifted_image = image.transform(
        (width, height), 
        Image.AFFINE, 
        (1, 0, shift_x, 0, 1, shift_y), 
        resample=Image.BICUBIC
    )
    
    return shifted_image
