import numpy as np
import math
import pickle
import pylab as pl

def get_gdata(my_red):
        #analyzing red color data by finding gaussian mean and covernce


        red= pickle.load(my_red)
        my_red.close()
        red_color = np.matrix(red)
        n1 = len(red[0])
        n2 = len(red[1])
        n3 = len(red[2])
        Red_mean = sum(red[0]) / n1
        Green_mean = sum(red[1]) / n2
        Blue_mean = sum(red[2]) / n3
        color_mean = [[Red_mean], [Green_mean], [Blue_mean]]

        k = red_color.shape
        color_cov = sum([(red_color[:, i] - color_mean) * (red_color[:, i] - color_mean).T for i in range(k[1])]) / (k[1] - 1)
        print(color_mean)
        print(color_cov)
        return [color_mean, color_cov]


def get_prob(red_color,color_mean, color_cov):
        a=1/math.sqrt(((2*math.pi) **3) *abs(np.linalg.det(color_cov)))
        b=math.exp((-0.5)*(red_color - color_mean).T * np.linalg.inv(color_cov) * (red_color - color_mean))
        prob=a*b
        return [prob]


def get_pic(img):
        # get the mean and coverance of my color data
red_mean = [[58.5286378072645], [121.76083497465945], [189.1032136974855]]
red_cov = [[770.30293194, -20.94969786, 341.1788335],
           [-20.94969786, 16.51113515, -40.15629527],
           [341.1788335, -40.15629527, 401.32332451]]

brown_mean = [[66.07455258020772], [111.9524788770173], [154.0496818513717]]
brown_cov = [[531.08422516, -163.82320883, 168.54420531],
             [-163.82320883, 79.42239822, -64.14464526],
             [168.54420531, -64.14464526, 105.25622688]]

notbred_mean = [[74.42037342628817], [114.38176997385645], [181.26536628780153]]
notbred_cov = [[364.16534328, -63.14704607, 87.58519275],
               [-63.14704607, 34.23617437, -62.46106007],
               [87.58519275, -62.46106007, 323.07301931]]

yellow_mean = [[160.4431735657226], [80.969922536916], [159.5479302832244]]

yellow_cov = [[1490.46817406, -183.6542845, -111.03658497],
              [-183.6542845, 296.54808761, -70.77326627],
              [-111.03658497, -70.77326627, 130.53180653]]


        array = img[::10, ::10, :]
        k = array[:, :, 0].shape
        pic = np.zeros((array.shape[0], array.shape[1], array.shape[2]))


        for i in range(k[0]):

                for j in range(k[1]):

                        color = [[array[i, j, 0]], [array[i, j, 1]], [array[i, j, 2]]]
                        my_color = np.matrix(color)
                        P_red = get_prob(my_color, red_mean, red_cov)
                        P_brown = get_prob(my_color, brown_mean, brown_cov)
                        P_notbred = get_prob(my_color, notbred_mean, notbred_cov)
                        P_yellow = get_prob(my_color, yellow_mean, yellow_cov)
                        # compare the gaussian probability,  1 when the red probability is the largest value among the four color
                        if max(P_red, P_brown, P_notbred, P_yellow) == P_red:
                                pic[i, j] = 0
                        elif max(P_red, P_brown, P_notbred, P_yellow) == P_brown:
                                pic[i, j] = 1
                        elif max(P_red, P_brown, P_notbred, P_yellow) == P_notbred:
                                pic[i, j] = 1
                        elif max(P_red, P_brown, P_notbred, P_yellow) == P_yellow:
                                pic[i, j] = 1


       # pl.imshow(pic)
       # pl.show()

        return (pic)