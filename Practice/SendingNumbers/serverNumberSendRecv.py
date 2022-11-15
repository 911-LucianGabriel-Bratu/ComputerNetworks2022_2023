import socket
import struct
from multiprocessing import Process
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
    mysocket.bind(('192.168.150.1', 8864))
    print("Binded the socket to ip 192.168.150.1 and port 8864")
    while True:
        mysocket.listen(5)
        print("Listening for incoming connections...")
        client_socket, addr = mysocket.accept()
        print("Accepted connection of client with address: " + str(addr))
        handle_client(client_socket)
        print("Execution stopped")


start_server()