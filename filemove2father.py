import os
import shutil

targetfile='/home/nrz/TestLab/frames/'

for filebox in os.listdir(targetfile):
    for pic in os.listdir(os.path.join(targetfile,filebox)):
        shutil.move(os.path.join(targetfile,filebox,pic),os.path.join(targetfile,pic))