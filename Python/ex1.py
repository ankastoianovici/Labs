#Sa se creez un script python care sa primeasca un fisier video ca input, iar la output sa creeze un folder care sa contina toate frame-urile video-ului. 
#Se poate alege orice fisier video.

import cv2
import os

video=cv2.VideoCapture("C:/Users/ankas/Videos/video.mp4")
Frame_Curent=0
#if not os.path.exist('C:/Users/ankas/Videos'):
    #os.makedirs('C:/Users/ankas/Videos')

while(True):
    success, frame =video.read()

    cv2.imshow("Output", frame)
    cv2.imwrite('C:/Users/ankas/Videos/frame'+ str(Frame_Curent)+ '.jpg', frame)
    Frame_Curent= Frame_Curent+1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

