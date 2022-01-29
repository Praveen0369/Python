import cv2
import os
import time
import uuid
IMAGES_PATH='Tensorflow\workspace\images\collectedimages'
#Labels Should be given here
labels =['hello','thanks','yes','no','iloveyou']
#----------
#no of images trained for a label
number_imgs=15
#---------
#labelling Collected Images
for label in labels:
    os.system ('Tensorflow\workspace\images\collectedimages\\'+label)
    cap=cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    #-------------
    #Geting Image for training
    for imgnum in range(number_imgs):
        ret,frame=cap.read()
        imgname=os.path.join(IMAGES_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname,frame)
        cv2.imshow('frame',frame)
        time.sleep(2)
        #-----------
        #press q to exit
        if cv2.waitKey(1)& 0xff==ord('q'):
            break
        cap.release()
        #_________
