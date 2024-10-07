# rotation of the given image by a certain angle
import cv2

img =cv2.imread (r"images/image4.jpeg")
angle=45
h, w = img.shape[:2]
M = cv2.getRotationMatrix2D((w/2, h/2), angle,1 )
rotated_img = cv2.warpAffine(img, M, (w,h))
cv2.imshow('Original Image', img)
cv2.imshow('Rotated Image', rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()