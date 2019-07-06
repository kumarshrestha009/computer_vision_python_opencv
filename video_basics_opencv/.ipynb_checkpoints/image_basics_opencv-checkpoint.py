import cv2
import numpy as np


ix = -1
iy = -1
drawing=False


#Function
def draw_rectangle(event,x,y,flags,param):
    global ix,iy,drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy = x,y
        
    elif event == cv2.EVENT_MOUSEMOVE:
        drawing=True
        cv2.rectangle(img,(ix,iy),(x,y),color=(0,255,0),thickness=-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing=False
        cv2.rectangle(img,(ix,iy),(x,y),color=(0,255,0),thickness=-1)
     
    
    
    
cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing',draw_rectangle)





#displaying image
img = np.zeros(shape=(512,512,3),dtype=np.int8)

while True:
    cv2.imshow('my_drawing',img)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()