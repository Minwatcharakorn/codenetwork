import socket
import threading
import sys

connected_clients = []

def broadcast_message(sender_client, message):
    for client_socket in connected_clients:
        if client_socket != sender_client:
            try:
                client_socket.sendall(message.encode("utf-8"))
            except:
                connected_clients.remove(client_socket)

def receive_messages(client_socket, address):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                print(f"Received from {address}: {message}")
                client_socket.sendall(message.encode("utf-8"))
                broadcast_message(client_socket, message)
        except:
            print(f"Connection closed with {address}.")
            if client_socket in connected_clients:
                connected_clients.remove(client_socket)
            break

def send_message(client_socket):
    while True:
        try:
            message = input()
            client_socket.sendall(message.encode("utf-8"))
        except:
            print("Connection closed.")
            break

def server():
    host = '10.4.15.78'  # IP address of the server (localhost)
    port = 12345       # Port to listen on

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server_socket.bind((host, port))
    except socket.error as e:
        print(str(e))
        sys.exit()

    print("Server listening on {}:{}".format(host, port))

    server_socket.listen(5)  # Maximum number of queued connections

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connected with {address}")

        connected_clients.append(client_socket)

        threading.Thread(target=receive_messages, args=(client_socket, address)).start()
        threading.Thread(target=send_message, args=(client_socket,)).start()

if __name__ == "__main__":
    server()
