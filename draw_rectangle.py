from PIL import Image, ImageOps,ImageDraw
img_dir="./input/HR.jpg"

img=Image.open(img_dir)
a=ImageDraw.ImageDraw(img)
a.rectangle((200,90,300,190),fill =None,outline ='red',width =2)
# img.show()
img.save("./output/rectangle.jpg")

#图片左上角为坐标原点
#水平为x，垂直为y
#参数为x1,y1,x2,y2