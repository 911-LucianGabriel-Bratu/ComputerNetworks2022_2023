import socket
import select
import threading


clients = []


def handle_client(client_socket):
    data = client_socket.recv(1024)
    data = data.decode()
    print(data)


if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 6969))
    server_socket.listen(5)
    read_list = [server_socket]
    ready, blank1, blank2 = select.select(read_list, [], [])
    for sock in ready:
        if sock is server_socket:
            #if the socket we are currently checking is the randevoux socket,
            #we accept incoming connections and append to the ready list and perform whatever storing operations
            #of the clients
            c_socket, c_address = sock.accept()
            ready.append(c_socket)
            clients.append(c_socket)
        else:
            try:
                #here we create threads for all client sockets we have stored
                client_thread = threading.Thread(target=handle_client, args=(sock,))
                client_thread.start()
                clients.remove(sock)
            except socket.error as err:
                print(err)
