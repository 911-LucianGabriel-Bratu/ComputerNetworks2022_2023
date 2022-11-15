import socket

flag = 0


def start_client():
    global flag
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Successfully created socket for client.")
    print("Attempting connection to server...")
    my_socket.connect(('192.168.150.1', 8864))
    print("Successfully connected to server")
    while True:
        line = input("Enter a string to send to the server: ")
        if line == "exit":
            flag = 1
        my_socket.send(line.encode())
        print("Successfully sent a string to the server")
        if flag:
            print("Execution stopped")
            return
        recv_line = my_socket.recv(1024)
        recv_line = recv_line.decode()
        print("The server sent back the string: " + recv_line)


start_client()