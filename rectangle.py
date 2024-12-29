import cv2 
import cvzone
cap=cv2.VideoCapture(0)
while True:
    success,imgg=cap.read()
    
    #adding rectangle for pointing out
    cv2.rectangle(imgg,(200,200),(500,400),(255,230,255),cv2.FILLED)
    cv2.putText(imgg,"CVZONE",(100,150),cv2.FONT_HERSHEY_PLAIN,5,(0,255,0),5)
    #adding text to rectangle
    '''cvzone.cornerRect(imgg,(200,200,300,200),
                        l=20,t=5,rt=1,
                        colorR=(250,0,250),colorC=(0,255,0))'''
    cvzone.putTextRect(imgg,"CVZONE",(200,150),border=5)
    cv2.imshow("Imagee",imgg)
    cv2.waitKey(1)

