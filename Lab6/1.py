# feature description using SIFT
# Import necessary libraries
import cv2
import matplotlib.pyplot as plt
import numpy as np
 
# Load the image from the specified path
image1 = cv2.imread('images/image4.jpeg')
 
# Check if the image is loaded correctly
if image1 is None:
    print("Error: Image not found.")
else:
    # Convert the training image to RGB
    training_image = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
 
    # Convert the training image to grayscale
    training_gray = cv2.cvtColor(training_image, cv2.COLOR_RGB2GRAY)
 
    # Create test image by adding Scale Invariance and Rotational Invariance
    test_image = cv2.pyrDown(training_image)
    test_image = cv2.pyrDown(test_image)
    num_rows, num_cols = test_image.shape[:2]
 
    rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), 30, 1)
    test_image = cv2.warpAffine(test_image, rotation_matrix, (num_cols, num_rows))
 
    test_gray = cv2.cvtColor(test_image, cv2.COLOR_RGB2GRAY)
 
    # Display training image and testing image
    fig, plots = plt.subplots(1, 2, figsize=(20, 10))
 
    plots[0].set_title("Training Image")
    plots[0].imshow(training_image)
    plots[0].axis('off')  # Hide axes for better visualization
 
    plots[1].set_title("Testing Image")
    plots[1].imshow(test_image)
    plots[1].axis('off')  # Hide axes for better visualization
 
    plt.show()

    # SIFT feature detection
    sift = cv2.SIFT_create()
    
    # Detect keypoints and descriptors for both images
    keypoints_train, descriptors_train = sift.detectAndCompute(training_gray, None)
    keypoints_test, descriptors_test = sift.detectAndCompute(test_gray, None)
    
    # Draw the keypoints on the images
    training_image_with_keypoints = cv2.drawKeypoints(training_image, keypoints_train, None)
    test_image_with_keypoints = cv2.drawKeypoints(test_image, keypoints_test, None)
    
    # Display the images with keypoints
    fig, plots = plt.subplots(1, 2, figsize=(20, 10))
    
    plots[0].set_title("Training Image with Keypoints")
    plots[0].imshow(training_image_with_keypoints)
    plots[0].axis('off')
    
    plots[1].set_title("Testing Image with Keypoints")
    plots[1].imshow(test_image_with_keypoints)
    plots[1].axis('off')
    
    plt.show()
