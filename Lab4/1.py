import cv2
import numpy as np

img = cv2.imread(r"images/image4.jpeg", cv2.IMREAD_GRAYSCALE)

if img is None :
    print("Error: Image not found")
else:
    #define kernel matrix
    kernel = np.ones((5,5), np.float32)/25

    #apply mean filtering
    mean_filtered = cv2.filter2D(img, -1, kernel)

    #apply median filtering
    median_filtered = cv2.medianBlur(img, 5)

    # sharpen the image using Laplacian operator
    sharpened_image = cv2.Laplacian(img, cv2.CV_64F)

    # convert sharpened image to 8-bit for diisplay
    sharpened_image = cv2.convertScaleAbs(sharpened_image)

    # display sharpened image
    cv2.imshow("original image", img)
    cv2.imshow("Mean filtered image",mean_filtered)
    cv2.imshow("Median filtered image", median_filtered)
    cv2.imshow("Sharpened image", sharpened_image)

    # wait for user input
    cv2.waitKey(0)

    # destroy all windows
    cv2.destroyAllWindows()