import socket
import pickle


if __name__ == "__main__":
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    crt_arr = []
    nr_input = int(input("Enter the amount of numbers in the array: "))
    for i in range(0, nr_input):
        el = int(input("Enter the number " + str(i) + " out of " + str(nr_input) + ":"))
        crt_arr.append(el)
    data = pickle.dumps(crt_arr)
    udp_socket.sendto(data, ('127.0.0.1', 6789))
    recv_data, address = udp_socket.recvfrom(4096)
    recv_data = recv_data.decode()
    print(recv_data)
