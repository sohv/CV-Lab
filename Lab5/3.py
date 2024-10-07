# translate an image
import numpy as np
import cv2

img = cv2.imread(r"images/image4.jpeg", 0)
rows, cols = img.shape
M = np.float32([[1,0,100], [0,1,50]])
dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()