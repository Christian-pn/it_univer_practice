from PIL import Image, ImageDraw, ImageFont

image = Image.new("RGB",(1024,1024), (255,255,255))
draw = ImageDraw.Draw(image)
fnt = ImageFont.truetype('System/Library/Fonts/Times.ttc', size= 250)   #System/Library/Fonts/   これはwindowsの為、実行できないので
draw.text((200, 500), "Hello", font = fnt, fill = (255,0,0))
image.show()