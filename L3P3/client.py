import socket
import struct
import threading


clients = []
my_mutex = threading.Lock()


def send_list(sock):
    return


def send_all():
    global clients
    for client in clients:
        send_list(client)


def server_talk(c_socket):
    #get the list of clients
    return


def client_talk(c_socket):
    #receive the chat from the other clients
    return


if __name__ == "__main__":
    global clients

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 6969))
    st = threading.Thread(target=server_talk, args=(s,))
    udp_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_s.sendto(b's', ('192.0.1.2', 6969))
    blank1, port = udp_s.getsockname()
    udp_s.bind(('0.0.0.0', port))
    ct = threading.Thread(target=client_talk, args=(s,))
    while True:
        msg = input("Enter a message: ")
        for c in clients:
            my_mutex.acquire()
            c.send(msg.encode())
            my_mutex.release()