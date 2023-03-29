import os

image_path='/home/nrz/下载/鱼道垃圾视频/trash_img'
txt_path='/home/nrz/下载/鱼道垃圾视频/trash_labels'
os.makedirs(txt_path,exist_ok=True)
image_list=os.listdir(image_path)

for image in image_list:
    image_name=image.split('.')[0]
    txt_name=image_name+'.txt'
    file=open(txt_path+'/'+txt_name,'w')
    file.close()