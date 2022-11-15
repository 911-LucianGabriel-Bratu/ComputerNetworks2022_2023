import socket


def handle_client(client_socket):
    recv_line = client_socket.recv(1024)
    recv_line = recv_line.decode()
    print("Received string: " + recv_line)
    while recv_line != "exit":
        recv_line += " had a stroke while coding with sockets"
        recv_line = recv_line.encode()
        client_socket.send(recv_line)
        print("Successfully sent the modified string back to client")
        recv_line = client_socket.recv(1024)
        recv_line = recv_line.decode()
        print("Received string: " + recv_line)


def start_server():
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Successfully created socket for server.")
    mysocket.bind(('192.168.150.1', 8864))
    print("Binded the socket to ip 192.168.150.1 and port 8864")
    mysocket.listen(5)
    print("Listening for incoming connections...")
    client_socket, addr = mysocket.accept()
    print("Accepted connection of client with address: " + str(addr))
    handle_client(client_socket)
    print("Execution stopped")


start_server()