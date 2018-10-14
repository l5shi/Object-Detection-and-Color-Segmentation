import numpy as np
from roipoly import roipoly
import cv2
import pylab as pl
import os
import pickle
from skimage import measure


# create image
my_pic=os.listdir('/Users/charles/Desktop/project/img')
Yellow_class=[[],[],[]]

for img_file in my_pic :

    img1 = cv2.imread('img/'+img_file)

    img2 = cv2.cvtColor(img1,cv2.COLOR_RGB2BGR)


    # show the image
    pl.imshow(img2)
    pl.colorbar()
    pl.title("left click: line segment         right click: close region")

    # let user draw first ROI in red color
    ROI1 = roipoly(roicolor='r') #let user draw first ROI

    # show the image with the first ROI
    ROI1.displayROI()
    # show the image with ROI and their mean values


    a=ROI1.getMask(img1)
    pl.imshow(a)
    pl.show()
    positions=np.where(a == True)

    imgy=cv2.cvtColor(img1,cv2.COLOR_RGB2YCR_CB)

    red = imgy[:, :, 0]
    green = imgy[:, :, 1]
    blue = imgy[:, :, 2]

    B=blue[positions]
    R=red[positions]
    G=green[positions]

    Yellow_class[0].extend(R.tolist())
    Yellow_class[1].extend(G.tolist())
    Yellow_class[2].extend(B.tolist())



my_yellowclass = open('yellowclass.pkl','wb')
pickle.dump(Yellow_class,my_yellowclass)
my_yellowclass.close()




