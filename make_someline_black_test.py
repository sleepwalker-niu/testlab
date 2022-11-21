import os

from PIL import Image




img = Image.open('test.jpg')
for w in range(img.width):
    for h in range(img.height):
        # w_true = w < 50 or w > 650
        h_true = h < 40 or h > 510
        light_true= w>292 and w<392 and h>233 and h<333
        if h_true or light_true:
            img.putpixel((w, h), 0)

img.save('result.jpg')



