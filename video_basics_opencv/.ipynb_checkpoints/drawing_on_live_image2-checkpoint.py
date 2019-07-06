import cv2
# from google.colab.patches import cv2_imshow


cap = cv2.VideoCapture(0)

width =int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

x = width//2
y = height//2

w = width//4
h = height//4


while True:
  ret,frame = cap.read()
  
  cv2.rectangle(frame, pt1=(x,y), pt2=(x+w,y+h), color=(255,0,0), thickness=3)
  
    
  cv2.imshow('frame',frame)
  
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()