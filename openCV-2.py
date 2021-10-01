import cv2
print(cv2.__version__)
cam=cv2.VideoCapture(0)
while True:
    #ret,frame=cam.read()
    ignore, frame =cam.read()
    grayframe=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("my webcam",frame)
    cv2.moveWindow("my webcam",0,0) #move window to 0,0
    cv2.imshow("my grayframe",grayframe)
    cv2.moveWindow("my grayframe",640,0) 

    cv2.imshow("my webcam2",frame)
    cv2.moveWindow("my webcam2",640,480) 
    cv2.imshow("my grayframe2",grayframe)
    cv2.moveWindow("my grayframe2",0,480) 
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()


