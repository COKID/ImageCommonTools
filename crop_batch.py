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
    # result=img.crop((280,155,390,265))#331
    # result=img.crop((460,280,560,380))
    # result=img.crop((60,240,130,310))
    # result=img.crop((120,240,220,340))
    # result=img.crop((200,90,300,190))#1115
    # result=img.crop((20,30,70,80))#euvp 8
    # result=img.crop((60,25,110,75))#euvp 23
    result=img.crop((285//4,150//4,410//4,275//4))#my
    result.save(join(out_dir,name))
    