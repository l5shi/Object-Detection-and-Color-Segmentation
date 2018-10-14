import cv2

import os
from find_color import myAlgorithm

folder="testset"
for filename in os.listdir(folder):

   img = cv2.imread (os.path.join(folder, filename))
   blX, blY,trX,trY,d = myAlgorithm(img)

   cv2.waitKey(0)
   cv2.destroyAllWindows()