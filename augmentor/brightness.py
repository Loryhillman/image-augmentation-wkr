from PIL import ImageEnhance

def change_brightness(image, factor=1.0):
    """
    Изменяет яркость изображения.

    :param image: изображение для изменения яркости
    :param factor: коэффициент яркости (1.0 — без изменений, <1 — темнее, >1 — ярче)
    :return: изображение с измененной яркостью
    """
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)