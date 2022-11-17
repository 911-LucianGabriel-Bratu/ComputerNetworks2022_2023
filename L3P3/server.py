import socket
import select
import struct


if __name__ == "__main__":
    clients = dict()
    rdv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    rdv.bind(('0.0.0.0', 6969))
    rdv.listen(5)
    read_list = [rdv]
    ready, blank1, blank2 = select.select(read_list, [], [])
    for sock in ready:
        if sock is rdv:
            cs, addr = sock.accept()
            ip = cs.recv(4)
            ip = ip.decode()
            p = cs.recv(4)
            p = struct.unpack('!I', p)
            clients[cs] = (ip, p)
            str_send = ""
            for client in clients:
                ip, port = clients.get(client)
                str_send = str_send + ip + str(port) + ";"
            cs.send(str_send.encode())
        else:
            try:
                sock.recv(100)
                clients.pop(sock)
                str_send = ""
                for client in clients:
                    ip, port = clients.get(client)
                    str_send = str_send + ip + str(port) + ";"
                for client in clients:
                    client.send(str_send.encode())
            except socket.error as e:
                print(e)
