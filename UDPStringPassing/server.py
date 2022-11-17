import socket


if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', 6969))
    data, address = server_socket.recvfrom(1024)
    print(data.decode())