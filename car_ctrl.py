import serial
import socket
import sys

def robocom(port=2222,serport="/dev/ttyACM0"):

	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.bind(("10.159.95.164",int(port)))
        
        ser=serial.Serial(serport,9600)
        try:
                while True:
                        cmd = s.recvfrom(1024)
                        ser.write(str(cmd[0]))
			print cmd[0]
        except:
                s.close()


if __name__=="__main__":
        if len(sys.argv)==3:
                robocom(sys.argv[1],sys.argv[2])
        elif len(sys.argv)==2:
                robocom(sys.argv[1])
        else:
                robocom()
