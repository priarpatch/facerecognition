import glob
import shutil
import os
import random
a=16
j=0
datadir=glob.glob('/*/*/ece196facerecognition/yaleB_faces/faceimagesp/*.jpg')
datadir=random.sample(datadir,len(datadir))
for i in datadir:
    j+=1
    if j<=(0.7*len(datadir)):
	    shutil.copy(i,'/home/pi/ece196facerecognition/data/Train/faceimagesp')
    elif j<=(0.8*len(datadir)) and j>(0.7*len(datadir)):
	    shutil.copy(i,'/home/pi/ece196facerecognition/data/Val/faceimagesp')
    else: 
	    shutil.copy(i,'/home/pi/ece196facerecognition/data/Test/faceimagesp')
