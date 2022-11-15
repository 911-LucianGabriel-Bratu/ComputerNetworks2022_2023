import socket
import time

if __name__ == '__main__':
    sfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sfd.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) # broadcast part

    for i in range(4):
        sfd.sendto(b'ping', ('127.30.255.255', 1729)) # 127.0.0.1 non broadcast
        t1 = time.time()
        response, addr = sfd.recvfrom(256)
        t2 = time.time()
        response = response.decode()

        if response == 'ping':
            print(float(t2 - t1))