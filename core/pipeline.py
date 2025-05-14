import random
from augmentor.rotate import rotate_image
from augmentor.flip import flip_image
from augmentor.noise import add_noise
from augmentor.shift import shift_image
from augmentor.brightness import change_brightness
from utils.helpers import resize_with_padding
from config.augmentation_config import augmentation_config

def apply_augmentation(image, target_size, augmentation_type):
    """ Применение выбранной аугментации """
    if augmentation_type == 'rotate' and augmentation_config['rotate']['enabled']:
        angle = augmentation_config['rotate']['params']['angle']
        print(f"Применяется угол: {angle} градусов")
        return rotate_image(image, angle=angle, target_size=target_size)

    elif augmentation_type == 'flip' and augmentation_config['flip']['enabled']:
        return flip_image(image)

    elif augmentation_type == 'noise' and augmentation_config['noise']['enabled']:
        noise_type = random.choice(augmentation_config['noise']['types'])

        if noise_type == 'gaussian':
            params = augmentation_config['noise']['params']['gaussian']
            return add_noise(image.convert('L'), noise_type='gaussian', std=params['std'])

        elif noise_type == 'salt_pepper':
            params = augmentation_config['noise']['params']['salt_pepper']
            return add_noise(
                image.convert('L'),
                noise_type='salt_pepper',
                amount=params['amount'],
                salt_vs_pepper=params['salt_vs_pepper']
            )


    elif augmentation_type == 'shift' and augmentation_config['shift']['enabled']:
        return shift_image(image, max_shift=augmentation_config['shift']['params']['max_shift'])

    elif augmentation_type == 'brightness' and augmentation_config['brightness']['enabled']:
        factor = random.uniform(augmentation_config['brightness']['params']['factor'], augmentation_config['brightness']['params']['factor'])  # Исправил, на случай диапазона
        return change_brightness(image, factor=factor)

    return image


def process_images(image, target_size, volume_level='low'):
    """ Обработка изображений с аугментациями в зависимости от объёма """
    image_resized = resize_with_padding(image, target_size)

    results = {}

    available_augmentations = ['rotate', 'flip', 'noise', 'shift', 'brightness']

    if volume_level == 'low':
        augmentations_to_apply = random.sample(available_augmentations, 2)
    elif volume_level == 'medium':
        augmentations_to_apply = random.sample(available_augmentations, 3)
        augmentations_to_apply = available_augmentations

    for augmentation in augmentations_to_apply:
        augmented_image = apply_augmentation(image_resized, target_size, augmentation)
        results[augmentation] = augmented_image

    return results