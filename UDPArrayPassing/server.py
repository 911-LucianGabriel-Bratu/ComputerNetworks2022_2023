import socket
import pickle


if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', 6789))
    data, address = server_socket.recvfrom(4096)
    array = pickle.loads(data)
    for i in range(0, len(array)):
        print(array[i])
    server_socket.sendto(b'poop gaming', address)
