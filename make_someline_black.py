import os

from PIL import Image

input_filepath='/home/nrz/daduriver工作文件/rgb2gray_output/_fortest/images'
output_filepath='/home/nrz/daduriver工作文件/rgb2gray_output/_fortest_cutedtopbottomcenter/images'
if not os.path.exists(output_filepath):
    os.makedirs(output_filepath)
input_filepath_list=os.listdir(input_filepath)
print(input_filepath_list)
for file in input_filepath_list:
    img = Image.open(os.path.join(input_filepath, file))
    for w in range(img.width):
        for h in range(img.height):
            #w_true = w < 50 or w > 650
            h_true = h < 40 or h > 510
            center_true = w > 292 and w < 412 and h > 233 and h < 373
            if h_true or center_true:
                img.putpixel((w, h), 0)
    img.save(os.path.join(output_filepath,file))

