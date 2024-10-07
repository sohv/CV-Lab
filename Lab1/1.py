import cv2

# load the image from the file
img = cv2.imread("images/image1.jpg")
# display the image in a window
cv2.imshow("Image", img)
# wait for they key press amd then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()