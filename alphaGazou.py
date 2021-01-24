from PIL import Image

image = Image.open("gz/koma2.png")
image2 = Image.open("koma.png")
image3 = Image.blend(image, image2, 0.5)
image3.show()
