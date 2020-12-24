from PIL import Image, ImageOps,ImageDraw
img_dir="rectangle.jpg"
img=Image.open(img_dir)
# img.show()
c=img.crop((50,0,530,480))
c.show()
# c.save("mpc.jpg")

#图片左上角为坐标原点
#水平为x，垂直为y
#参数为x1,y1,x2,y2