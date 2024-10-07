import cv2
import numpy as np
 
# Load the input video
cap = cv2.VideoCapture('videos/video1.mp4')
 
# Read the first frame and convert it to grayscale
ret, first_frame = cap.read()
if not ret:
    print("Error: Couldn't read the video.")
    exit()
 
prev_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
 
# Create a mask for drawing the optical flow vectors
mask = np.zeros_like(first_frame)
mask[..., 1] = 255  # Set saturation to maximum for colorful display
 
while cap.isOpened():
    # Capture the next frame
    ret, frame = cap.read()
    if not ret:
        break
 
    # Convert the current frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    # Calculate the optical flow between the previous and current frame
    flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
 
    # Calculate the magnitude and angle of the flow vectors
    magnitude, angle = cv2.cartToPolar(flow[..., 0], flow[..., 1])
 
    # Set the mask’s hue to the angle of the flow
    mask[..., 0] = angle * 180 / np.pi / 2
 
    # Normalize the magnitude to the range 0 to 255
    mask[..., 2] = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)
 
    # Convert the mask to a BGR image
    rgb_flow = cv2.cvtColor(mask, cv2.COLOR_HSV2BGR)
 
    # Overlay the flow on the original frame
    output = cv2.addWeighted(frame, 1, rgb_flow, 2, 0)
 
    # Display the result
    cv2.imshow('Optical Flow', output)
 
    # Break the loop if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
    # Update the previous frame to the current frame
    prev_gray = gray.copy()
 
# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()
