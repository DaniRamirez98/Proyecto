import numpy as np
from PIL import Image
import io

def preprocess_image(image_bytes, target_size=(64, 64)):
    """
    Load an image, resize it, convert to grayscale, and normalize it.
    """
    img = Image.open(io.BytesIO(image_bytes))
    img = img.convert('L') # Convert to grayscale
    img = img.resize(target_size)
    img_array = np.array(img).flatten() / 255.0 # Normalize and flatten
    return img_array

def load_and_preprocess_images(image_list, target_size=(64, 64)):
    """
    Process a list of image bytes into a NumPy array.
    """
    processed_images = []
    for img_bytes in image_list:
        processed_images.append(preprocess_image(img_bytes, target_size))
    return np.array(processed_images)
