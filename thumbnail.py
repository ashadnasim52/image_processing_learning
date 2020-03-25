from PIL import Image

img = Image.open('./images/trunks.png')
img.thumbnail((400, 100))
img.save('thumbnail.png', 'png')
