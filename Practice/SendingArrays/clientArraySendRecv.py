import socket
import pickle
import struct


def start_client():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect(("localhost", 2064))
    if my_socket == -1:
        print("Socket could not connect")
    print("Successfully connected the socket to the server")
    while True:
        array = []
        nr = int(input("Enter the amount of numbers in the array: "))
        for i in range(0, nr):
            array.append(int(input("Enter a number for the array: ")))
        data_to_send = pickle.dumps(array)
        my_socket.send(data_to_send)
        print("Successfully sent the array to the server")
        received_data = my_socket.recv(1024)
        received_data = pickle.loads(received_data)
        print("Received: " + repr(received_data))
        received_min = my_socket.recv(1024)
        received_min = struct.unpack("!I", received_min)[0]
        print("Minimum in the array is: " + str(received_min))


start_client()
