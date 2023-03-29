import os
import shutil
targetfile='/home/nrz/daduriver工作文件/rgb2gray_input/dataset_dirtywater_fortest_copy/images'
formatfile='/home/nrz/daduriver工作文件/rgb2gray_output/_fortest_select_copy/images'
savefile='/home/nrz/daduriver工作文件/rgb2gray_input/dataset_dirtywater_fortest_select/images'

if not os.path.exists(savefile):
    os.makedirs(savefile)

targetfile_list=os.listdir(targetfile)
formatfile_list=os.listdir(formatfile)
count=0
for target_img in targetfile_list:
    target_img_name=target_img.split('.')[0]
    print(target_img_name+" yes!")
    if target_img in formatfile_list:
        shutil.copyfile(os.path.join(targetfile,target_img),os.path.join(savefile,target_img))
        count=count+1
        print(count)
