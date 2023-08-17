import socket
import threading
import sys

def receive_messages(client_socket, address):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                print(f"Received from {address}: {message}")
        except:
            print(f"Connection closed with {address}.")
            break

def send_message(client_socket):
    while True:
        message = input()
        client_socket.sendall(message.encode("utf-8"))

def client():
    host = '10.4.15.78'  # IP address of the server (localhost)
    port = 12345       # Port to connect to

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
    except socket.error as e:
        print(str(e))
        sys.exit()

    threading.Thread(target=receive_messages, args=(client_socket, host)).start()
    threading.Thread(target=send_message, args=(client_socket,)).start()


if __name__ == "__main__":
    client()
       