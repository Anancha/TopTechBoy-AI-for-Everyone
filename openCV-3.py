import cv2
print(cv2.__version__)
widht = 640
height = 360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,widht)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))   # MJPG is the codec
while True:
    ignore, frame =cam.read()
    cv2.imshow("my webcam",frame)
    cv2.moveWindow("my webcam",0,0) #move window to 0,0
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()

