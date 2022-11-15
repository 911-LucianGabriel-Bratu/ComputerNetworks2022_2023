import socket
from random import randint
import struct

generated_number = randint(0, 100)
print("Generated global number: " + str(generated_number))


def handle_client(client):
    while True:
        nr_recv = struct.unpack('!I', client.recv(4))[0]
        print("Received number from client: " + str(nr_recv))
        if nr_recv == generated_number:
            client.send(b"Correct")
            print("Sent message to client")
            client.close()
            return
        elif nr_recv < generated_number:
            client.send(b"Higher")
            print("Sent message to client")
        else:
            client.send(b"Lower")
            print("Sent message to client")


def server_start():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.bind(('192.168.150.1', 1270))
    my_socket.listen()
    print("Listening for connections...")

    while True:
        client, address = my_socket.accept()
        print("Client connected")
        handle_client(client)


server_start()
