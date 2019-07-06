'''You only have one task here. Create a program that reads in a live stream from a camera on your computer (or if you don't have a camera, just open up a video file). Then whenever you click the left mouse button down, create a blue circle around where you've clicked.'''

import cv2

cap = cv2.VideoCapture(0)

#CALLBACK FUNCTINS
def draw_rectangle(event,x,y,flags,param):
    global pt1,button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        
        if button_clicked==False:
            pt1=(x,y)
            button_clicked=True
    elif event == cv2.EVENT_LBUTTONUP:
        pt1=(0,0)
        button_clicked = False

        



#GLOBAL VARIABLE
pt1=(0,0)
button_clicked = False




#CONNECTING TO CALLBACK
cv2.namedWindow('frame')
cv2.setMouseCallback('frame',draw_rectangle)





while True:
    
    ret,frame = cap.read()
    if button_clicked:
        cv2.circle(frame, center=pt1, radius=30, color=(0,0,255), thickness=3)


    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()