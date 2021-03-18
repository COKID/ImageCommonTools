import random
from PIL import Image, ImageOps
from scipy import misc
import numpy as np
from os import listdir
from os.path import join
import os
import torch.nn as nn

sf=2
input_dir = r"./input/"

filenames = [join(input_dir, x) for x in listdir(input_dir)]

length=len(filenames)
def up():
    for i in range(length):
        _, filename = os.path.split(filenames[i])
        image=Image.open(filenames[i]).convert('RGB')#RGB L YCbCr

        SR_image=image.resize((image.size[0]*sf,image.size[1]*sf),Image.BICUBIC)
        SR_image.save("./output/"+str(sf)+"/"+filename)
        print(i+1, filename)

def down():
    for i in range(length):
        _, filename = os.path.split(filenames[i])
        image=Image.open(filenames[i]).convert('RGB')#RGB L YCbCr

        SR_image=image.resize((image.size[0]//sf,image.size[1]//sf),Image.BICUBIC)
        path="./output/"+str(sf)+"/"
        if not os.path.exists(path):
            os.makedirs(path)
        SR_image.save(path+filename)
        print(i+1, filename)

if __name__ == '__main__':
    # for sf in [2,4,8]:
        down()
