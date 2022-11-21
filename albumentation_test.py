import albumentations as A
from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os


def imgaug(img_name,img_path,img_savepath):
    img=cv2.imread(img_path)

    albu=A.Compose([
        A.RandomBrightnessContrast(brightness_limit=0.2,always_apply=True,p=1),
        A.MotionBlur(blur_limit=17,always_apply=True,p=1),
        A.RandomFog(p=1,fog_coef_upper=0.5)

    ])
    img_afteraug=albu(image=img)['image']
    cv2.imwrite(os.path.join(img_savepath,'allaug'+img_name),img_afteraug)

if __name__=="__main__":
    image_filepath='testimagefile'
    image_savepath='testimagesavefile'
    image_list=os.listdir(image_filepath)
    for image in image_list:
        imgaug(image,os.path.join(image_filepath,image), image_savepath)





