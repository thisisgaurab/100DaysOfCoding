import os

import numpy as np
import skimage.io
from skimage import io
from skimage.util import img_as_float

directory_path = '/Users/gaurab/PycharmProjects/Numpy/Colin_Powell'

contents = os.listdir(directory_path)
result = np.zeros((250, 250, 3), dtype=np.float64)
num_images = 0


for content in contents:
    file_path = os.path.join(directory_path, content)
    if os.path.isfile(file_path):
        img = io.imread(file_path)
        img = img_as_float(img)

        if img.shape == (250, 250, 3):
            result += img
            num_images += 1

if num_images>=1:
    average_img = result/num_images

    average_img = (average_img*255).astype(np.uint8)

    # save the averaged result with skimage.io.imsave
    output_path = '/Users/gaurab/PycharmProjects/Numpy/averaged_img.png'
    skimage.io.imsave(output_path, average_img)
    print(f'The average image is saved to {output_path}.')
else:
    print('No image of the perfect shape is found.')



