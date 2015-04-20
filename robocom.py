import serial
import socket
import sys

import signal, os

def handler(signum, frame):
    print 'Signal handler called with signal', signum
    raise IOError("Couldn't recieve!")

def robocom(port=2222,serport="/dev/ttyACM0"):
        s=socket.socket()
        s.bind(('',int(port)))
        s.listen(1)
        cs,address=s.accept()
        #signal.signal(signal.SIGALRM, handler)
        ser=serial.Serial(serport,9600)
        try:
                while True:
                        try:
                                #signal.alarm(2)
                                cs.sendall("cmd> ")
                                cmd=cs.recv(20)
                                print str(cmd)
                                ser.write(str(cmd))
                                #signal.alarm(0) 
                        except IOError:
                                #ser.write('r')
                                ser.write('s')
                                #ser.write('r')
                                ser.write('s')
                                #ser.write('r')
                                ser.write('s')
        finally:
                ser.write('s')
                s.close()
                cs.close()


if __name__=="__main__":
        if len(sys.argv)==3:
                robocom(sys.argv[1],sys.argv[2])
        elif len(sys.argv)==2:
                robocom(sys.argv[1])
        else:
                robocom()
