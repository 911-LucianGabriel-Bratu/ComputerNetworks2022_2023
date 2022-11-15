import socket
import random
import struct


if __name__ == '__main__':
    try:
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print("Error :" + e.strerror)
        exit(-1)
    my_socket.connect(('localhost', 8573))
    print("Successfully connected to the server.")
    lwpt = 1
    uppr = 2**10-1
    random.seed()

    finished = False
    steps = 0

    data = my_socket.recv(1024)
    data = data.decode()
    print(data)

    while not finished:
        my_num = random.randint(lwpt, uppr)
        og = my_num
        my_num = struct.pack('!I', my_num)
        try:
            my_socket.sendall(my_num)
            answer = my_socket.recv(1)
        except socket.error as e:
            print("Error: " + e.strerror)
            exit(-1)
        steps += 1
        answer = answer.decode()
        if answer == 'H':
            lwpt = og
        elif answer == 'L':
            uppr = og
        elif answer == 'W' or answer == 'E':
            finished = True
            my_socket.close()
    if answer == 'W':
        print("I guessed the number: " + str(og) + " in " + str(steps) + " steps.")
    else:
        print("I lost...")
