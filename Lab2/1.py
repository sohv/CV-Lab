# load the image and display it in grayscale
# also display the image dimensions both original and grayscale
import cv2

imgnew=cv2.imread(r"images/image2.jpg")
imgnew=cv2.resize(imgnew,(780,540))
cv2.imshow("Image",imgnew)
cv2.waitKey(0)
cv2.destroyAllWindows()

dimensions1=imgnew.shape

print("Dimensions of Original: ",dimensions1)

gray_image = cv2.cvtColor(imgnew, cv2.COLOR_BGR2GRAY)

cv2.imshow("Grayscale",gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

dimensions2=gray_image.shape
print("Dimensions of Grayscale: ",dimensions2)

print("Pixel at (200,250): ", gray_image[200][250])
gray_new=gray_image
gray_new[0:200,0:200]=1

cv2.imshow("Grayscale New",gray_new)
cv2.waitKey(0)
cv2.destroyAllWindows()