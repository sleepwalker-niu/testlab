import os

from PIL import Image

targetfilepath='/home/nrz/VOCdevkit/VOC2012/JPEGImages'
outputpath='/home/nrz/VOCdevkit/VOC2012/JPEGImages'
if not os.path.exists(outputpath):
    os.makedirs(outputpath)
targetfilelist=os.listdir(targetfilepath)
print(targetfilelist)
for file in targetfilelist:
    img=Image.open(os.path.join(targetfilepath,file))
    print(len(img.split()))
    L=img.convert("L")
    RGB=L.convert('RGB')
    RGB.save(os.path.join(outputpath,file))
    print(len(RGB.split()))

