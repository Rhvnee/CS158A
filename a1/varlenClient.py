from socket import *

serverName = 'localhost' #ip
serverPort = 12000 #port num

#TCP Socket Stream
clientSocket = socket(AF_INET, SOCK_STREAM)

#Connect to Server
clientSocket.connect((serverName, serverPort))

sentence = input('Input sentence: ')

clientSocket.send(sentence.encode()) #Sends sentence to Server

modifiedSentence = clientSocket.recv(64) #Recieve modified sentence from Server

print('From Server:', modifiedSentence.decode()) #Print modified Sentence
