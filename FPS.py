import cv2
import time

# Initialize variables for FPS calculation
start_time = time.time()
frame_count = 0

# Initialize the camera to capture the image
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 30)  # Set fps to 30

while True:
    # Read the frame from the camera
    success, img = cap.read()

    # Increment frame count
    frame_count += 1

    # Calculate FPS every second
    if time.time() - start_time >= 1:
        fps = frame_count / (time.time() - start_time)
        print(f"FPS: {fps:.2f}")
        start_time = time.time()
        frame_count = 0

    # Display the frame
    cv2.imshow("Image", img)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture object and close the window
cap.release()
cv2.destroyAllWindows()
