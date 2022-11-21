import os

image_filepath=''
label_filepath=''

imagelist=os.listdir(image_filepath)
labellist=os.listdir(label_filepath)
label_need2remove=[]

for image in imagelist:
    imagename=image.split()[0]
    labelname_shouldbe=imagename+'.txt'
    for label in labellist:
        labelname=label.split()[0]
        if imagename == labelname:
            label_need2remove.append(label)
