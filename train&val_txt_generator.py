import os

inputpath='/home/nrz/daduriver工作文件/VOCdevkit/VOC2012/JPEGImages'
outputpath='/home/nrz/daduriver工作文件/VOCdevkit/VOC2012/ImageSets/Main'

files=os.listdir(inputpath)
e=open(os.path.join(outputpath,'val.txt'),'a+')
for file in files:
    filename=file.split('.')[0]
    e.writelines(filename+'\n')
e.close()