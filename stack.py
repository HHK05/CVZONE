import cv2
import cvzone

cap = cv2.VideoCapture(0)

# Start an infinite loop to continually capture frames
while True:
    # Read image from the camera
    success, img = cap.read()

    # Convert image to grayscale
    imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Resize the image to be smaller
    imgSmall = cv2.resize(img, (0, 0), None, 0.1, 0.1)

    # Resize the image to be larger
    imgLarger = cv2.resize(img, (0, 0), None, 3, 3)

    # Apply Canny edge detection on the grayscale
    imgGreyCanny = cv2.Canny(imgGrey, 50, 150)

    # Convert the image to HSV color space
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    img_list = [img, imgGrey, imgGreyCanny, imgHSV, imgSmall, imgLarger]

    # Stack the images together using cvzone stackImages function
    stackedImg = cvzone.stackImages(img_list, 2, 0.7)

    # Display the stacked image
    cv2.imshow("Stacked Images", stackedImg)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture object and close the window
cap.release()
cv2.destroyAllWindows()
