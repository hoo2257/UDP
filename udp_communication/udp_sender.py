import socket

send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = ("127.0.0.1", 9999)

send_socket.sendto(data, dest)