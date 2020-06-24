from PIL import Image, ImageOps,ImageDraw
img=Image.open("img.jpg")
a=ImageDraw.ImageDraw(img)
a.rectangle((280,155,390,265),fill =None,outline ='red',width =2)
img.save("rectangle.jpg")

#图片左上角为坐标原点
#水平为x，垂直为y
#参数为x1,y1,x2,y2