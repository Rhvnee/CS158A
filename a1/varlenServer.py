from socket import *
from socket import socket

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM) #create TCP socket, empty ' ' means listens to all)

serverSocket.bind(('', serverPort)) #bind socket to port

serverSocket.listen(1) #listen for connections

while True:
    cnSocket, addr = serverSocket.accept() #Accept connection

    length_bytes = cnSocket.recv(2)

    msg_length = int.from_bytes(length_bytes, byteorder='big')

    x = int(length_bytes.decode('utf-8')) #Convert byte to int
    print('received msg length:', x)

    sentence = cnSocket.recv(x).decode() #recieve rest of sentence, but only to the specified int
    print('received msg:', sentence)

    if sentence == 'exit':
        cnSocket.send("exiting".encode())
        break

    else:
        print('msg length sent: ', x)
        capSentence = sentence.upper() #Convert to uppercase
        cnSocket.send(capSentence.encode()) #send sentence back
        cnSocket.close() #close connection