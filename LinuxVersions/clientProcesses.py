import socket
import struct

flag = 0

def start_client():
    global flag
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Successfully created socket for client.")
    print("Attempting connection to server...")
    my_socket.connect(('localhost', 3350))
    print("Successfully connected to server")
    while True:
        nr = int(input("Enter a number to send to the server: "))
        if nr == 0:
            flag = 1
        nr = struct.pack('!I', nr)
        my_socket.send(nr)
        print("Successfully sent a number to the server")
        if flag:
            print("Execution stopped")
            return
        recv_number = my_socket.recv(1024)
        recv_number = struct.unpack('!I', recv_number)[0]
        print("The server sent back the number: " + str(recv_number))


start_client()
