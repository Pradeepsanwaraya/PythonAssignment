from PIL import Image

image = Image.open("myimage.png")

print("Format:", image.format)
print("Size:", image.size)
print("Mode:", image.mode)

image.show()
