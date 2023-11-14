'''image editor python code file'''
import os
from PIL import Image, ImageEnhance, ImageFilter

PATH = './imgs'
PATH_OUT = './editedImgs'

for filename in os.listdir(PATH):
    if filename.endswith('jpeg') or filename.endswith('jpg'):
        img = Image.open(f"{PATH}/{filename}")

        edit = img.filter(ImageFilter.SHARPEN).rotate(-90)
        FACTOR = 1.5
        enhancer = ImageEnhance.Contrast(edit)
        edit = enhancer.enhance(FACTOR)

        clean_name = os.path.splitext(filename)[0]

        edit.save(f"{PATH_OUT}/{clean_name}_edited.jpg")
        edit.close()
