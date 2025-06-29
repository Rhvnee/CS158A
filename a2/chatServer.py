import socket
import threading

clients = []

def take_client(client_socket, client_address):

    port = client_address[1]

    print(f"Client {port} connected.")

    while True:

        try:

            message = client_socket.recv(1024).decode()

            if not message:

                break

            if message.lower() == "exit":

                print(f"Client {port} disconnected.")

                client_socket.close()
                clients.remove(client_socket)

                break

            deliver_message = f"{port}: {message}"

            print(f"Received from {port}: {message}")

            for client in clients:

                if client != client_socket:

                    client.send(deliver_message.encode())

        except:

            if client_socket in clients:

                clients.remove(client_socket)

            client_socket.close()
            break


def start_server():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 12000))
    server.listen(10)
    print("Server is listening on port 12000...")

    while True:

        client_socket, client_address = server.accept()
        clients.append(client_socket)

        thread = threading.Thread(target=take_client, args=(client_socket, client_address))
        thread.start()

if __name__ == "__main__":
    start_server()
