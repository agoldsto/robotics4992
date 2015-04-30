import struct, socket

s_listen = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#s_listen.bind(("192.168.1.247",2222))
s_listen.bind(("10.159.95.164",2221))
buff = s_listen.recvfrom(1024)

print buff

val_list = buff[0].split()
string = ''
for i in range(0, len(val_list)):
	string = string + ' ' + val_list[i]

cval_list = struct.pack('<40s', string)

while True:
	s_send = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
	s_send.sendto(cval_list,("10.159.212.237",2221))
                
