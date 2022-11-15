#lab3 pb 3
import select
import socket

# learn to send any type of data: for
import struct


def send_clients(client_socket, clients_list):
    sz = clients_list.size()
    sz = struct.pack('!I', sz)
    client_socket.send(sz)
    for client in clients_list:
        addr = client[0] + ',' + str([1])
        client_socket.send(addr)


def update_clients(clients_sockets, clients_list):
    for i in range(1, len(clients_sockets)):
        send_clients(clients_sockets[i], clients_list)


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind('0.0.0.0', 1234)
    sock.listen(3)

    inputs = [sock]
    outputs = []
    clients = []
    clients_sockets = []
    while True:
        readable, writable, exceptional = select.select(inputs, outputs, inputs)
        for fd in readable:
            if fd is sock:  # TCP connection handling
                (cs, address) = sock.accept()
                inputs.append(cs)
                clients_sockets.append(cs)
                clients.append(address)
                update_clients(inputs, clients)
            else:
                data = fd.recv(256)
                index = inputs.index(fd)
                clients.remove(clients[index-1])
                inputs.remove(fd)
                update_clients(inputs, clients)
