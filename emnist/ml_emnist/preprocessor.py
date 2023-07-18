"""
Preprocessing for new data input
"""

import numpy as np
from PIL import Image

def preproc(img_file) -> np.ndarray:
    """
    loads image from file,
    converts image to grey scale,
    applies linear transformations (change of black and white) and normalization
    """
    img = Image.open(img_file)
    img = img.convert(mode="L")
    img_arr = np.asarray(img)
    img_arr = (img_arr * (-1) + 255) / 255
    img_arr = img_arr.reshape((1,28,28,1))

    return img_arr
