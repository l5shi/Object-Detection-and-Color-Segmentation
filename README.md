# Object-Detection-and-Color-Segmentation



In this project, I am supposed to extract useful data of the red barrel and other colors’ from the given pictures by using roipoly function. The resulting information, which includes red barrel area, barrel distance, colors, and etc., generated a database for me to classify a testing picture. By using the database I got from previous training pictures, I trained a Gaussian Mixture Model (GMM) to find where the barrel is located and then I took out the red region by using Find Contour function. At last, I trained a linear regression model to approximate the barrel’s distance.




