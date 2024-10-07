import cv2
import numpy as np

img = cv2.imread(r"images/image4.jpeg")

if img is None :
    print("Error: Image not loaded")
    exit()

# convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply gaussian blur to remove noise
blur = cv2.GaussianBlur(gray, (5,5), 0)

# apply sobel operator to detect edges in x and y operator
sobelx = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)

#combine the edges detected in x and y directions using magnitude
edges = np.sqrt(sobelx**2 + sobely**2)

# convert the magnitude to an 8-bit image
edges = np.uint8(np.absolute(edges))

# optionally apply binary threshold to highlight edges
_, edges = cv2.threshold(edges, 50, 255, cv2.THRESH_BINARY)

# display the threshold image and edge-detected image
cv2.imshow('Original image', img)
cv2.imshow('Edge-detected Image', edges)

# save the edge detected image
cv2.imwrite('images/output2.jpg', edges)

# wait for user to close the window
cv2.waitKey(0)

cv2.destroyAllWindows()