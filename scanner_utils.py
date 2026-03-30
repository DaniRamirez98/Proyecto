import cv2
import numpy as np
from pyzbar.pyzbar import decode
from PIL import Image

def decode_barcode(image_data):
    """
    Decodes barcode from image data.
    image_data can be a PIL Image or a numpy array.
    Returns the decoded data as a string if found, else None.
    """
    if isinstance(image_data, Image.Image):
        # Convert PIL image to numpy array (OpenCV format)
        image_data = np.array(image_data)
        image_data = cv2.cvtColor(image_data, cv2.COLOR_RGB2BGR)

    decoded_objects = decode(image_data)
    for obj in decoded_objects:
        # Return the first barcode found
        return obj.data.decode("utf-8")

    return None
