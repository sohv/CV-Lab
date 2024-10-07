import cv2

# load the image
img = cv2.imread(r"images/image2.jpg")

# convert the input image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# compute the negative of the grayscale image
neg = cv2.bitwise_not(gray)

cv2.imshow("Input image", img)
cv2.imshow("Negative Image", neg)

# wait for the key press
key = cv2.waitKey(0)

# save the negative image if s key is pressed
if key == ord('s'):
    cv2.imwrite('negative_image.jpg', neg)

# destroy all windows
cv2.destroyAllWindows()