# perform log transformation in the image
import cv2
import numpy as np

image = cv2.imread(r"images/image2.jpg")

# define gamma value for gamma correction
gamma = 1.5

# define constant c for transformation
C = 20

#convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# perform log transformation
log = C * np.log(1 + gray.astype(np.float64))

# normalize the log transformed image to be in the range [0,255]
logimg = cv2.normalize(log, None, 0, 255, cv2.NORM_MINMAX)

# convert logimg to uint8 type
logimg = np.uint8(logimg)

# display the input and output images side by side
result = cv2.hconcat([gray, logimg])

cv2.imshow("Log Transformation", result)

# save the output image
cv2.imwrite("images/output1.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()