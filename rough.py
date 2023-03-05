
from tkinter import *
from tkinter import filedialog

import matplotlib.pyplot as plt
import numpy
import numpy as np
from skimage.transform import resize
from PIL import Image, ImageTk
image = Image
water_img = np.array(image.open("pythonwatermark.png"))
img = np.array(image.open("test.png"))

small_waterimg = resize(water_img, (100, 100))
for i in small_waterimg:
    for b in i:
        if b.any() == np.array([0, 0, 0, 0]).all():
            b += [1, 1, 1, 1]

img = np.array(img) / 255
img[50:150, -150:-50, :] = small_waterimg
plt.imshow(img)
plt.show()
