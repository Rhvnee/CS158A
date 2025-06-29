import socket
import threading

def receive_messages(sock):

    while True:

        try:

            message = sock.recv(1024).decode()

            if not message:

                break

            print(message)

        except:

            break

def main():

    serverName = 'localhost'
    serverPort = 12000
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    # Start thread to receive messages
    threading.Thread(target=receive_messages, args=(clientSocket,), daemon=True).start()

    print("You can now start chatting. Type 'exit' to quit.")

    while True:

        msg = input()

        clientSocket.send(msg.encode())

        if msg.lower() == 'exit':

            break

    clientSocket.close()

if __name__ == "__main__":
    main()
