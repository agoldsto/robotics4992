import numpy as np
import cv2
import time
import sys
#import serial
#ser=serial.Serial("/dev/ttyACM0",9600)
import socket
s=socket.socket()
s.connect(("127.0.0.1",int(sys.argv[1])))
time.sleep(1)
cap = cv2.VideoCapture(0)
cap.set(3,160)#640
cap.set(4,120)#480
hasblue=lambda mask: any(map(any,mask))
while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Display the resulting frame
        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # define range of blue color in HSV
        lower_blue = np.array([110, 50, 50], dtype=np.uint8)#red
        upper_blue = np.array([130,255,255], dtype=np.uint8)#red

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
#       xs=[]
#       ys=[]
        M=cv2.moments(mask)
#       if mask.any():
#               for i in range(len(mask)):
#                       if any(mask[i]):
#                               for j in range(len(mask[i])):
#                                       if mask[i][j]==255:
#                                               ys.append(i)
#                                               xs.append(j)
#       xa=sum(xs)/(len(xs)+1)
#       ya=sum(ys)/(len(ys)+1)
#       p=(xa,ya)
        #time.sleep(.25)
#       s.sendall(str(xa))
        #serport="/dev/ttyACM0"
        #ser=serial.Serial(serport,9600)
        ###ser.write(str(xa))
        ###r,framedot=cap.read()
        maskbgr=cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
#       cv2.circle(maskbgr,p,5,[255,0,0],5)
        #cv2.circle(framedot,p,5,[255,0,0],5)
#       print "p: "+str(p)
        xa=int(M["m10"]/(M['m00']+1))
        ya=int(M["m01"]/(M['m00']+1))
        p=(xa,ya)
        cv2.circle(maskbgr,p,5,[255,0,0],5)
        print "p: "+str(p)
        s.sendall(str(xa))
        # Bitwise-AND mask and original image
        ###res = cv2.bitwise_and(frame,frame, mask= mask)

        #cv2.imshow('frame',frame)
        #cv2.imshow('framedot',framedot)
        #cv2.imshow('mask',mask)
        cv2.imshow('maskbgr',maskbgr)
        #cv2.imshow('res',res)

        #cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break

