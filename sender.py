import struct, socket
boolean = 1

while boolean == 1:

        print("1   Send Command String")
        print("2   Receive Current Values")
        print("3   Exit Program \n")
        option = raw_input("Select Option: ")
        print "\n"

        if option == '1':

                message = raw_input("Input Command String: ")

                command = struct.pack('<40s', message)
                #'>20s20s20s20s20s20s20s20s20s20s',cmd_list[0],cmd_list[1],cmd_list[2], cmd_list[3], cmd_list[4], cmd_list[5], cmd_list[6], cmd_list[7], cmd_list[8], cmd_list[9])

                print command
                s_send = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
                s_send.sendto(command,("10.159.95.164",2221))

                print "\n"
                
        elif option == '2':

                s_listen = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                s_listen.bind(("10.159.212.237",2221))
                buff = s_listen.recvfrom(1024)

                val_list = buff[0].split()
                
                print val_list[0] + " = " + val_list[1]
                print val_list[2] + " = " + val_list[3]
                print val_list[4] + " = " + val_list[5]
                print val_list[6] + " = " + val_list[7]
                print val_list[8] + " = " + val_list[9]

                print "\n"
                
        elif option == '3':

                boolean = 2

        else:

                print("Invalid Input \n")





