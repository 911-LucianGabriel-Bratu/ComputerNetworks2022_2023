import socket
import struct


def start():
    clients_list = []
    my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_sock.bind(('172.30.113.166', 1731))
    print("Successfully created server socket.")
    my_sock.listen()
    print("Listening for incoming connections...")

    while True:
        client, address = my_sock.accept()
        print("Accepted connection from client.")
        client_name = client.recv(16).decode()
        client_password = client.recv(16).decode()
        print("Client with username: " + str(client_name) + " and password: " + str(client_password) + " successfully connected.")
        clients_list.append((client, address))


start()