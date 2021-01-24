from PIL import Image, ImageDraw

image = Image.new("RGB",(1024,1024), (255,255,255))
draw = ImageDraw.Draw(image)
draw.line((100,100,400,400), fill = (255,0,0), width = 10)
draw.rectangle((100,600,500,800), fill =(0,0,255))
draw.ellipse((600,500,800,700), fill = 0, outline= (0,255,0))
image.show()