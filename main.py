from PIL import Image


image = Image.open('image.jpg')
pixels = image.load()

colors = []

for x in range(image.width):
    for y in range(image.height):
        if image.getpixel((x, y)) not in colors:
            colors.append(image.getpixel((x, y)))


print(len(colors))
