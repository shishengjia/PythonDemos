from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('> ')
    if not data:
        break
    #python3默认使用的是str类型对字符串编码，默认使用bytes操作二进制数据流
    #所以在发送文件前需要对内容进行编码

    tcpCliSock.send(data.encode()+'\r\n'.encode())
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    # 解码
    print(data.strip().decode())
    tcpCliSock.close()
