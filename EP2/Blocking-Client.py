import socket

sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
sock.connect(('localhost', 1234))

data = 'foobar\n' * 1 * 1024 * 1024 
assert sock.send(data.encode()) == len(data.encode())
