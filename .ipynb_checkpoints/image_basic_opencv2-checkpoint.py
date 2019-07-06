import cv2
import numpy as np


#Function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),50,(0,255,0),-1)
#         cv2.rectangle(img,(x,y),(200,200),(255,255,255),-1)

cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing',draw_circle)





#displaying image
img = np.zeros(shape=(512,512,3),dtype=np.int8)

while True:
    cv2.imshow('my_drawing',img)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()

#function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
    
        cv2.circle(img,(x,y),100,color=(255,255,255),thickness=-1)
   


cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing',draw_circle)








# #showing image
# img = np.zeros(shape=(512,512,3),dtype=np.int16)
# while True:
#     cv2.imshow('my_drawing',img)
#     if cv2.waitkey(1) & 0xFF == 27:
#         break
    
# cv2.destroyAllWindows()