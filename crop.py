from PIL import Image, ImageOps,ImageDraw
img=Image.open("img.jpg")
img.show()
c=img.crop((280,155,390,265))
c.save("drm.jpg")

#图片左上角为坐标原点
#水平为x，垂直为y
#参数为x1,y1,x2,y2