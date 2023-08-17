import socket

HOST = "10.4.15.71"
PORT = 50005

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s :
    s.connect((HOST,PORT))
    s.sendall(b'HELLO , WORLD')
    data = s.recv(1024)

print('Received', repr(data))