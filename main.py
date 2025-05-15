import os
from PIL import Image
from core.pipeline import process_images
from utils.helpers import is_grayscale, resize_with_padding
from img_io.image_loader import load_image
from img_io.image_saver import save_image
from config.augmentation_config import augmentation_config

INPUT_DIR = 'data/input'
OUTPUT_DIR = 'data/output'
TARGET_SIZE = (128, 128)
VOLUME_LEVEL = 'high'

def main():

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    filenames = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))]

    if not filenames:
        print("Нет изображений в папке input.")
        return

    for filename in filenames:
        path = os.path.join(INPUT_DIR, filename)
        image = load_image(path)

        if not is_grayscale(image):
            print(f"Пропущено: {filename} — не полутоновое изображение.")
            continue

        base_name, _ = os.path.splitext(filename)

        augmented_images = process_images(image, TARGET_SIZE, volume_level=VOLUME_LEVEL)

    for i, aug_img in enumerate(augmented_images):
        output_filename = f"{base_name}_aug_{i:03d}.png"
        output_path = os.path.join(OUTPUT_DIR, output_filename)
        save_image(aug_img, output_path)
        print(f"Аугментированное изображение {i+1} сохранено → {output_filename}")
if __name__ == "__main__":
    main()
