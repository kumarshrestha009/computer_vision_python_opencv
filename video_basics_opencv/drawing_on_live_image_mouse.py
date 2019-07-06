import cv2
# from google.colab.patches import cv2_imshow


cap = cv2.VideoCapture(0)

#CALLBACK FUNCTIONS
def draw_rectangle(event,x,y,flags,param):
    global pt1,pt2,topleft_clicked,buttomright_clicked
    if event==cv2.EVENT_LBUTTONDOWN:
        
        #RESETING THE RECTANGLE
        if topleft_clicked and buttomright_clicked:
            pt1=(0,0)
            pt2=(0,0)
            topleft_clicked=False
            buttomright_clicked=False
        
        if topleft_clicked==False:
            pt1=(x,y)
            topleft_clicked=True
        elif buttomright_clicked==False:
            pt2=(x,y)
            buttomright_clicked=True




#GLOBAL VARIABLE
pt1=(0,0)
pt2=(0,0)
topleft_clicked=False
buttomright_clicked=False




#CONNECTING TO CALLBACK
cv2.namedWindow('frame')
cv2.setMouseCallback('frame',draw_rectangle)



while True:
  ret,frame = cap.read()
  
  if topleft_clicked==True:
    cv2.circle(frame, center=pt1, radius=5, color=(0,0,255), thickness=3)
  if topleft_clicked and buttomright_clicked:
    cv2.rectangle(frame,pt1=pt1,pt2=pt2,color = (0,0,255),thickness=3)

  cv2.imshow('frame',frame)
  
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()