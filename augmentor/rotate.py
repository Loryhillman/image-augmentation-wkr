from PIL import Image

def rotate_image(image: Image.Image, angle: float, target_size: tuple[int, int]) -> Image.Image:
    """
    Поворачивает изображение на заданный угол с последующим приведением к заданному размеру.

    :param image: Исходное изображение.
    :param angle: Угол поворота в градусах.
    :param target_size: Размер для ресайза после поворота.
    :return: Повернутое и масштабированное изображение.
    """
    rotated_image = image.rotate(angle, expand=True, resample=Image.BICUBIC)
    return rotated_image.resize(target_size, resample=Image.BICUBIC)