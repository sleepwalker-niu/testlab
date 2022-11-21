import os

from PIL import Image

targetfilepath='testimagesavefile'
outputpath='grayimage'
if not os.path.exists(outputpath):
    os.makedirs(outputpath)
targetfilelist=os.listdir(targetfilepath)
print(targetfilelist)
for file in targetfilelist:
    img=Image.open(os.path.join(targetfilepath,file))
    print(len(img.split()))
    L=img.convert("L")
    L.save(os.path.join(outputpath,file))
    print(len(L.split()))

