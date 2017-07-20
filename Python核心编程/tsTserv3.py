# -*- encoding: utf-8 -*-
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    addr = (HOST, 21568)
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ).decode()
        if not data:
            break
        bytes_message = (ctime() + data).encode()
        tcpCliSock.send(bytes_message)
    tcpCliSock.close()
