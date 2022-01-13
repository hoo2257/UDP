import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

recv_address = ("", 9999)
print("bind1")
sock.bind(recv_address)
print("bind2")
data_size = 32

while True:

    recv, _ = sock.recvfrom(data_size)
    data = str(recv, encoding="utf-8")
    temp = data.split(" ")
    signal_type = int(temp[1])
    timestamp = float(temp[2])
    signal = float(temp[3])


    if signal_type == 0:
        BVP = signal
        print("BVP ", BVP)

    elif signal_type == 1:
        GSR = signal
        print("GSR ", GSR)












