import cv2
from g_data import get_pic
import pylab as pl
import numpy as np
from plot_ols import l_reg
import pickle
import os

def myAlgorithm(test_img):
#load my color data
    my_color_red=open('redclass.pkl','rb')
    my_color_brown=open('brownclass.pkl','rb')
    my_color_notbred=open('NotBarrelRedclass.pkl','rb')
    my_color_yellow=open('yellowclass.pkl','rb')
    redd_area=open('redarea.pkl','rb')
    red_area= pickle.load(redd_area)
    red_distance=[10,10,14,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,7,7,7,7,8,8,8,8,9,9]
    my_linear = l_reg(red_area,red_distance)



    #read test image and conver them from RGB into YCR_CB

    #test_img=cv2.imread('test/001.png')
    imgg=cv2.cvtColor(test_img,cv2.COLOR_RGB2BGR)
    imgy=cv2.cvtColor(test_img,cv2.COLOR_RGB2YCR_CB)


    array = imgg[::10, ::10, :]
    array1 = imgg[::10, ::10, :]
    temp = cv2.cvtColor(array1,cv2.COLOR_RGB2BGR)
    temp1 = cv2.cvtColor(temp,cv2.COLOR_BGR2RGB)

    k = array[:, :, 0].shape
    img1 = get_pic(imgy)

    for i in range (k[0]):
        for j in range (k[1]):

            if any(img1[i,j])== 1:
                array[i, j, :] = 0


    img2 = cv2.cvtColor(array,cv2.COLOR_RGB2GRAY)
    ret, thresh = cv2.threshold(img2, 0, 255, 0)
    imgx, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)



    #mask = np.zeros(temp1.shape, dtype="uint8")
    #pl.imshow(mask)
    #pl.show()

    area=[]
    for c in contours:
         area.append(cv2.contourArea(c))
       #rotrect = cv2.minAreaRect(c)
       #box = cv2.boxPoints(rotrect)
       # box = np.int0(box)
       # cv2.drawContours(temp1, [box], 0, (255,255,255), 1)
    my_area=max(area)
    final_area=my_area
    final_area1=final_area*100;

    for i in range (len(area)):
        if ((area[i]!=my_area) & (area[i]/my_area > 0.2)):
            final_area=final_area+area[i]


    for c in contours:
        area1=cv2.contourArea(c)
        if (area1==my_area):
            rotrect = cv2.minAreaRect(c)
            box = cv2.boxPoints(rotrect)
            box = np.int0(box)
            cv2.drawContours(temp1, [box], 0, (0,0,255), 1)
            #print('coordinates:')

            #print(box)
            a=[]
            c=[[],[]]
            xx=0
            d=[[],[]]
            yy=0
            a=sum(box)/len(box)
            for i in range (4):
                  if (box[i][0] > a[0]):
                        c[xx]=box[i]
                        xx=xx+1

            if(c[0][1]<c[1][1]):

                e=c[0]
            elif(c[0][1]>c[1][1]):
                e=c[1]



            for j in range (4):
                  if (box[j][0] < a[0]):
                        d[yy]=box[j]
                        yy=yy+1

            if(d[0][1]>d[1][1]):

                f=d[0]
            elif(d[0][1]<d[1][1]):
                f=d[1]

            print('top right coordinates:')
            print(e)
            print('bottom left coordinates:')
            print(f)
            xx = 0
            yy = 0



    #        width, height=rotrect[1]

    print('distance:')

    distance=my_linear[0]*final_area1+my_linear[1]
    #my_area=max(index)


    print(distance)
    pl.imshow(temp1)
    pl.show()
    return (d[0],d[1],f[0],f[1],distance)

