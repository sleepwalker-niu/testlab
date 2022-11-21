import os
import shutil
labelspath='/home/nrz/daduriver工作文件/rgb2gray_output/_fortrain_sixspecies_aug/labels/val'
labelsfilelist=os.listdir(labelspath)
for labelfile in labelsfilelist:
    shutil.copy(os.path.join(labelspath,labelfile),os.path.join(labelspath,'albuaug'+labelfile))
