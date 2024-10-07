# scaling of an image
import numpy as np
import cv2

# Read the image
img = cv2.imread(r"images/image4.jpeg", 0)

# Check if the image was loaded successfully
if img is None:
    print("Error: Image not found or unable to load.")
else:
    # Get the dimensions of the image
    rows, cols = img.shape

    # display the original image
    cv2.imshow('Original Image', img)
    
    # Resize the image to shrink it
    img_shrinked = cv2.resize(img, (250, 200), interpolation=cv2.INTER_AREA)
    cv2.imshow('Shrinked Image', img_shrinked)

    # Resize the image to enlarge it
    img_enlarged = cv2.resize(img_shrinked, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    cv2.imshow('Enlarged Image', img_enlarged)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()