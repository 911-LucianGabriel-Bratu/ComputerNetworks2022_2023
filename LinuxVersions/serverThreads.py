import socket
import threading
import struct
import random

client_guessed = False
my_lock = threading.Lock()
server_number = random.randint(1, 2**10-1)
print("Server number is: " + str(server_number))
winner_thread = 0
threads = []
client_count = 0


def handle_client(c_socket):
    global client_guessed, my_lock, winner_thread, client_count
    my_id = client_count
    message = "Hello client " + str(my_id) + "! You are now part of the number guessing competition!"
    c_socket.sendall(message.encode())
    while not client_guessed:
        try:
            client_number = c_socket.recv(1024)
            client_number = struct.unpack('!I', client_number)[0]
            if client_number < server_number:
                c_socket.sendall(b'H')
            elif client_number > server_number:
                c_socket.sendall(b'L')
            elif client_number == server_number:
                my_lock.acquire()
                client_guessed = True
                winner_thread = threading.get_ident()
                my_lock.release()
        except socket.error as se:
            print("Error " + se.strerror)
            break
    if client_guessed:
        if threading.get_ident() == winner_thread:
            c_socket.sendall(b'W')
            print("We have a winner!", c_socket.getpeername())
            print("Thread: " + str(my_id) + " winner.")
        else:
            c_socket.sendall(b'E')
            print("Thread: " + str(my_id) + " did not guess the number.")
    c_socket.close()


if __name__ == '__main__':
    try:
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.bind(('localhost', 8573))
        my_socket.listen(5)
    except socket.error as se:
        print("Error: " + se.strerror)
        exit(-1)

    while True:
        client_socket, address = my_socket.accept()
        t = threading.Thread(target=handle_client, args=(client_socket,))
        threads.append(t)
        client_count += 1
        t.start()
