
import cv2
from g_data import get_pic
import pylab as pl
import numpy as np
import math
import pickle




def l_reg(area,dis):

      x= np.ones((len(area),1))
      y=np.matrix(area).T
      z=np.matrix(dis).T
      data=np.concatenate((y,x),axis=1)
      my_linear=(data.T * data).I * data.T * z


      return (my_linear)