import cv2
import cvzone

img_url = "https://www.google.com/search?q=python&sca_esv=591263652&rlz=1C1CHBF_enIN987IN987&tbm=isch&sxsrf=AM9HkKneVO0AyWwOH9TWnraClUlU7s33dg:1702660985834&source=lnms&sa=X&ved=2ahUKEwiX4u65-pGDAxVBZmwGHVVmBF0Q_AUoAXoECAEQAw&biw=1163&bih=501&dpr=1.65#imgrc=FWZwbDvOyoiVTM"  
img_normal = cvzone.downloadImageFromUrl(url=img_url)
img_png = cvzone.downloadImageFromUrl(url=img_url, keepTransparency=True)

img_png = cv2.resize(img_png, (0, 0), None, 3, 3)

cv2.imshow("Image Normal", img_normal)
cv2.imshow("Transparent Image", img_png)
cv2.waitKey(0)
