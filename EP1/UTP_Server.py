import socket

host = "10.4.15.76"
port = 2000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((host, port))

    while True:
        data, addr = s.recvfrom(1024)
        print("Received data from", addr, ": ", data.decode())

        s.sendto(data, addr)