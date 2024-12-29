import cv2
import cvzone
import numpy as np 

cap = cv2.VideoCapture(0)

img_URL = "https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/gigs/325052855/original/b625a4f04d18c9ace8c2430c6d0aa7cdb861296e/create-softwares-in-python.jpg"
img_PNG = cv2.imread(img_URL)
alpha_channel = np.ones(img_PNG.shape[:2], dtype=img_PNG.dtype) * 255
img_PNG = cv2.merge((img_PNG, alpha_channel))

while True:
    # Read the image from the camera frame
    success, img = cap.read()

    # Overlay the image at different positions
    imgOverlay1 = cvzone.overlayPNG(img, img_PNG, pos=[-30, 50])
    imgOverlay2 = cvzone.overlayPNG(imgOverlay1, img_PNG, pos=[200, 200])
    imgOverlay3 = cvzone.overlayPNG(imgOverlay2, img_PNG, pos=[500, 400])

    cv2.imshow("ImageOverlay", imgOverlay3)
    
    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture object and close the window
cap.release()
cv2.destroyAllWindows()
