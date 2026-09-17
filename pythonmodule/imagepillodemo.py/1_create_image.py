from PIL import Image

image = Image.new("RGB", (400, 300), "white")
image.save("myimage.png")

print("Image created successfully")
