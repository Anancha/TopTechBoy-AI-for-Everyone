import cv2
print(cv2.__version__)

rows = int(input('Boss, How many Row do you want?:'))
column = int(input('Boss, How many Column do you want?:'))
widht = 1280
height = 720
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,widht)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))   # MJPG is the codec
while True:
    ignore, frame =cam.read()
    frame = cv2.resize(frame,(int(widht/column),int(height/column)))    
    for i in range(0,rows):
        for j in range(0,column):
            windName='Window'+str(i)+' x ' +str(j)
            cv2.imshow(windName,frame)
            cv2.moveWindow(windName,int(widht/column)*j,int(height/column+30)*i)
             
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()

