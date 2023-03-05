from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
from skimage.transform import resize
from PIL import Image, ImageTk

image =Image

window = Tk()
window.title("image water marker")
window.config(padx=100,pady=100)
img = np.array([0])
water_img = np.array([0])

checked_state1 = IntVar()
checkbutton = Checkbutton(text="status",variable=checked_state1)
checkbutton.grid(column=1,row=2)

checked_state2 = IntVar()
checkbutton = Checkbutton(text="status",variable=checked_state2)
checkbutton.grid(column=2,row=2)


def show():
    global img
    global water_img
    watsec = img[50:150, -150:-50, :]
    if water_img.shape != (1,) and img.shape != (1,):
        small_waterimg = resize(water_img, (100, 100))
        for i in range(len(small_waterimg)):
            for b in range(len(small_waterimg[i])):
                if small_waterimg[i,b].any() == np.array([0, 0, 0, 0]).any():
                    small_waterimg[i,b] += watsec[i,b]

        img = np.array(img) / 255
        img[50:150, -150:-50, :] = small_waterimg
        plt.imshow(img)
        plt.show()

def open_image():
    global img
    global water_img
    file_path = filedialog.askopenfilename()
    img = np.array(Image.open(file_path))
    checked_state1.set(1)
    show()

def open_water():
    global img
    global water_img
    file_path = filedialog.askopenfilename()
    water_img = np.array(Image.open(file_path))
    checked_state2.set(1)
    show()


upimg_button = Button(text="upload Image", command=open_image)
upimg_button.grid(column=1,row=1)
upwat_button = Button(text="upload water mark", command=open_water)
upwat_button.grid(column=2,row=1)


window.mainloop()


