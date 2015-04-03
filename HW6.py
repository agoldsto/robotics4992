import serial
import socket
import sys
import time
def com(port=2222,dev="/dev/ttyACM0"):
        s=socket.socket()
        s.bind(('',int(port)))
        s.listen(1)
        cs,ca=s.accept()
        ser=serial.Serial(str(dev),9600)
        encodeA=lambda v :hex(int(v)%160)[2:].decode('hex')
        a='P'
        try:
                while(1):
                        cmd=cs.recv(3)
                        print 'cmd: '+str(cmd)
                        try:
                                a=encodeA(cmd)
                                #a=int(cmd)%160
                        except:
                                pass
                        ser.write(a)
                        print 'sent: ' + str(a)
                        #print 'recieved: '+ser.readline()
                        #if a=='P':
                                #time.sleep(.1)
        finally:
                s.close()
                cs.close()

if __name__ =="__main__":
    if len(sys.argv)==3:
        com(sys.argv[1],sys.argv[2])
    elif len(sys.argv)==2:
        com(sys.argv[1])
    else:
        com()


