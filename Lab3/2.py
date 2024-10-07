import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"images/image3.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Setting the grid size
plt.figure(figsize = (20, 20))

# Plotting the original image
plt.subplot(221)
plt.title('Original')
plt.imshow(img)

# Plotting the histogram for the image
img_hist = cv2.calcHist([img_1], [0], None, [256], [0, 256])
plt.subplot(222)
plt.title('Histogram 1')
plt.plot(img_hist)

# Plotting the histogram using the ravel function
plt.subplot(223)
plt.hist(img_1.ravel(), 256, [0, 256])
plt.title('Histogram 2')

# Applying the Histogram equalization using the cv2.equalizeHist() function
final_img = cv2.equalizeHist(img_1)

# Display the histogram
plt.show()

# Displaying the image
cv2.imshow('Histogram Equalization', final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()