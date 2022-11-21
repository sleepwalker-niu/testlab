import os
import cv2
import numpy as np

imagedir='/home/nrz/daduriver工作文件/need2transfercolor'
outputdir='/home/nrz/daduriver工作文件/transfercolor_res'

if not os.path.exists(outputdir):
    os.makedirs(outputdir)

imagelist=os.listdir(imagedir)

for img in imagelist:
    input_path=os.path.join(imagedir,img)
    Is = cv2.imread(input_path)
    Ir = cv2.imread(
        '/home/nrz/TestLab/colortransfer_images/2022-07-10-22-17-330000000000.jpg')
    # plt.imshow(Ir[...,::-1])
    # plt.show()
    # plt.imshow(Is[...,::-1])
    # plt.show()
    # BGR->LAB
    LabIs = cv2.cvtColor(Is, cv2.COLOR_BGR2LAB)
    LabIr = cv2.cvtColor(Ir, cv2.COLOR_BGR2LAB)
    # mean、std
    Is_means = [0, 0, 0]
    Ir_means = [0, 0, 0]
    Is_stdevs = [0, 0, 0]
    Ir_stdevs = [0, 0, 0]
    LabIs = LabIs.astype(np.float32) / 255.
    LabIr = LabIr.astype(np.float32) / 255.
    for i in range(3):
        Is_means[i] += LabIs[:, :, i].mean()
        Ir_means[i] += LabIr[:, :, i].mean()
        Is_stdevs[i] += LabIs[:, :, i].std()
        Ir_stdevs[i] += LabIr[:, :, i].std()
    thresh = [a / b for a, b in zip(Ir_stdevs, Is_stdevs)]
    LabIt = thresh * (LabIs - Is_means) + Ir_means

    # [0-255]
    LabIt = (LabIt * 255.)
    LabIt *= (LabIt > 0)
    LabIt = (LabIt * (LabIt <= 255) + 255 * (LabIt > 255)).astype(np.uint8)

    # show
    It = cv2.cvtColor(LabIt, cv2.COLOR_LAB2BGR)
    cv2.imwrite(os.path.join(outputdir,img), img=It)