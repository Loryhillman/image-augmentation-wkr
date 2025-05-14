from PIL import Image

def is_grayscale(image):

    if image.mode in ("L", "LA"):
        return True
    elif image.mode == "RGB":

        pixels = image.load()
        for i in range(image.width):
            for j in range(image.height):
                r, g, b = pixels[i, j]
                if r != g or g != b:
                    return False
        return True
    return False

def resize_with_padding(image, target_size):
    width, height = image.size
    aspect_ratio = width / height

    if aspect_ratio > 1:
        new_width = target_size[0]
        new_height = int(target_size[0] / aspect_ratio)
    else:
        new_height = target_size[1]
        new_width = int(target_size[1] * aspect_ratio)

    image_resized = image.resize((new_width, new_height), Image.LANCZOS)
    new_image = Image.new("RGB", target_size, (255, 255, 255))
    new_image.paste(image_resized, ((target_size[0] - new_width) // 2, (target_size[1] - new_height) // 2))

    return new_image