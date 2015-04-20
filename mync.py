import socket
import sys

def mync(adder,port):
	ap=(str(adder),int(port))
	s=socket.socket()
	s.connect(ap)
	s.setblocking(0)
	try:
		while(True):
			try:
				cmd=raw_input(s.recv(0x8000))
				s.sendall(cmd)
			except socket.error:
				continue
	except:
		s.close()

	
if __name__=="__main__":
	mync(sys.argv[1],sys.argv[2])
