import socket

if __name__ == '__main__':
    sfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sfd.bind(('0.0.0.0', 1729))

    while True:
        respone, addr = sfd.recvfrom(256)
        print(respone.decode())
        sfd.sendto(respone, addr)