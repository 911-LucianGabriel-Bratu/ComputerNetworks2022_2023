import socket
import struct


def client_registration():
    my_tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_tcpsock.connect(('172.30.113.166', 1731))
    c_user = input("Enter username: ")
    c_password = input("Enter password: ")
    print("Sending data to server...")
    my_tcpsock.send(c_user.encode())
    my_tcpsock.send(c_password.encode())
    print("Successfully sent data to server.")


def start():
    # my_UDPsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP socket
    client_registration()


start()