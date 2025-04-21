import socket
from base64 import encode

#创建socket对象
client_socket=socket.socket()
#连接哪个主机
ip='199.1.8.41'
port=80
client_socket.connect((ip,port))
print('.........与服务器的连接成功............')
#发送数据
client_socket.send('welcome to python world'.encode('utf-8'))
#闭socket
client_socket.close()
print('发送完毕')