import socket
import struct
import os

def handle_client(client_socket):
    print("Pid: " + str(os.getpid()))
    recv_number = client_socket.recv(1024)
    recv_number = struct.unpack('!I', recv_number)[0]
    print("Received number: " + str(recv_number))
    while recv_number != 0:
        recv_number += 10
        recv_number = struct.pack('!I', recv_number)
        client_socket.send(recv_number)
        print("Successfully sent number back to client")
        recv_number = client_socket.recv(1024)
        recv_number = struct.unpack('!I', recv_number)[0]
        print("Received number: " + str(recv_number))
    exit(1)


def start_server():
    print("Pid: " + str(os.getpid()))
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Successfully created socket for server.")
    mysocket.bind(('localhost', 3350))
    print("Binded the socket to ip 192.168.1.255 and port 3350")
    while True:
        mysocket.listen(5)
        print("Listening for incoming connections...")
        client_socket, addr = mysocket.accept()
        print("Accepted connection of client with address: " + str(addr))
        pid = os.fork()
        if pid == 0:
            handle_client(client_socket)
        print("Execution stopped")


start_server()