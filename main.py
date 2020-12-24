from os import listdir
from os.path import join
import os
from PIL import Image, ImageOps

img_dir="./input/"
out_dir="./output/"
img_filename=listdir(img_dir)
img_full_dir = [join(img_dir, x) for x in listdir(img_dir)]

for name,path in zip(img_filename,img_full_dir):
    img=Image.open(path)
    # result=img.crop((230,180,320,270))
    result=img.crop((280,155,390,265))
    result.save(join(out_dir,name))
    