from PIL import Image

def rotate_image(image: Image.Image, angle: float, target_size: tuple = None) -> Image.Image:
    """
    Поворачивает изображение на заданный угол.
    Если указан target_size, то после поворота изменяет размер.

    :param image: Исходное изображение.
    :param angle: Угол поворота в градусах.
    :param target_size: Размер для ресайза (ширина, высота). Необязательный.
    :return: Повернутое изображение (и изменённого размера, если задан target_size).
    """
    rotated_image = image.rotate(angle, expand=True, resample=Image.BICUBIC)

    if target_size:
        return rotated_image.resize(target_size, resample=Image.BICUBIC)

    return rotated_image