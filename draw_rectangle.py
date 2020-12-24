from PIL import Image, ImageOps,ImageDraw
img_dir="./img/hr.jpg"

img=Image.open(img_dir)
a=ImageDraw.ImageDraw(img)
a.rectangle((230,180,320,270),fill =None,outline ='red',width =2)
# img.show()
img.save("rectangle.jpg")

#图片左上角为坐标原点
#水平为x，垂直为y
#参数为x1,y1,x2,y2