from PIL import Image, ImageOps,ImageDraw
from os import listdir
from os.path import join
import os

img_dir="./input/"
out_dir="./output/"
img_filename=listdir(img_dir)
img_full_dir = [join(img_dir, x) for x in listdir(img_dir)]

for name,path in zip(img_filename,img_full_dir):
    img=Image.open(path)
    a=ImageDraw.ImageDraw(img)
    a.rectangle((120,240,220,340),fill =None,outline ='red',width =2)
    # img.show()
    img.save(join(out_dir,"rectangel_"+name))

#图片左上角为坐标原点
#水平为x，垂直为y
#参数为x1,y1,x2,y2