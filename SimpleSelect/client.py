import socket


if __name__ == "__main__":
    #simple string passing from client to server
    #the client can be extended to perform other things
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 6969))
    message = input("Enter a message to be sent to the server: ")
    client_socket.send(message.encode())