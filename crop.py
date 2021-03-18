from PIL import Image, ImageOps,ImageDraw
img_dir="./input/红外.jpg"
img=Image.open(img_dir)
# img.show()
c=img.crop((285*4,150*4,410*4,275*4))
c.show()
c.save("./output/crop.jpg")

#图片左上角为坐标原点
#水平为x，垂直为y
#参数为x1,y1,x2,y2