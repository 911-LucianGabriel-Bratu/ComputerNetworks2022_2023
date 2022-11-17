import socket
import pickle
import struct


def sort_array(arr):
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                x = arr[i]
                arr[i] = arr[j]
                arr[j] = x
    return arr


def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        data_arr = pickle.loads(data)
        print("Received array: " + repr(data_arr))
        data_arr = sort_array(data_arr)
        print("Sorted array: " + repr(data_arr))
        minim = data_arr[0]
        data_arr = pickle.dumps(data_arr)
        client_socket.send(data_arr)
        print("Successfully sent the modified array to the client.")
        minim = struct.pack('!I', minim)
        client_socket.send(minim)
        print("Successfully sent the minimum in the array to the client.")


def start_server():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.bind(("localhost", 2064))
    if my_socket == -1:
        print("Could not create socket")
    my_socket.listen(5)
    print("Listening for new connections...")
    client_socket, addr = my_socket.accept()
    print("Accepted a new connection: " + str(addr))
    handle_client(client_socket)


start_server()