from PIL import Image
from resizeimage import resizeimage


def compress_image(img, dest_filename, size):
    with open(img, 'r+b') as f:
        with Image.open(f) as image:
            if not size:
                size = [100, 100]
            cover = resizeimage.resize_cover(image, size)
            filename = dest_filename
            cover.save(filename, image.format)
