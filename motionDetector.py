import cv2
from cv2 import imshow
import numpy as np


capture=cv2.VideoCapture(0)
var=0
while True:
    check,frame=capture.read()
    flip=cv2.flip(frame,1) #our main frame
    if var==0:
     base=flip
     var=1
     continue

    bgray=cv2.cvtColor(base,cv2.COLOR_BGR2GRAY)
    fgray=cv2.cvtColor(flip,cv2.COLOR_BGR2GRAY)
    ret,binBase=cv2.threshold(bgray,125,255,cv2.THRESH_BINARY)
    ret,binFlip=cv2.threshold(fgray,125,255,cv2.THRESH_BINARY)
    
    img=cv2.bitwise_xor(binBase,binFlip)
    #imshow("show",img)  #bitwise result

    nonzero=np.sum(img==255)
    total=img.shape[0]*img.shape[1]
  
    if ((nonzero/total)*100)>3: #accuracy is detected here
        print("movement detected")
        cv2.putText(flip,"movement detected !!",(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),3)

     
    cv2.imshow("video",flip)
    base=flip
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
 

    