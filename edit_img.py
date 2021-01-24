from PIL import Image

image = Image.open("koma.png")
#image.show()

output_image = image.rotate(45)
output_image.show()
output_image.save("output.png")