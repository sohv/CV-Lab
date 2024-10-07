import cv2

# open the video file
cap = cv2.VideoCapture('videos/video1.mp4')
# loop through frames in the video
while cap.isOpened():
    # read a frame
    ret, frame = cap.read()
    # check if the frame was successfully read
    if ret:
        # display the frame on the screen
        cv2.imshow('Video', frame)
        # wait for a key press for 25 milliseconds
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
        else:
            break
    # release the video capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()