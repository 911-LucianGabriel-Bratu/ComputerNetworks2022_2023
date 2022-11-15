import socket
from random import randint
import struct


def client_start():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect(('192.168.150.1', 1270))
    a = randint(0, 100)
    print("Generated number: " + str(a))
    initial_number = a
    a = struct.pack('!I', a)
    my_socket.send(a)

    while True:
        print("Waiting for server response...")
        message = my_socket.recv(256)
        print("Received response from server")
        if message == b"Lower":
            new_a = randint(0, initial_number)
            print("Generated number: " + str(new_a))
            initial_number = new_a
            new_a = struct.pack('!I', new_a)
            my_socket.send(new_a)
        elif message == b"Correct":
            print('I guessed correctly. The number was: ' + str(initial_number))
            return
        else:
            new_a = randint(initial_number, initial_number + 10)
            print("Generated number: " + str(new_a))
            initial_number = new_a
            new_a = struct.pack('!I', new_a)
            my_socket.send(new_a)



client_start()
