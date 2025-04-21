import socket
#创建socket对象
clinet_socket=socket.socket()
clinet_socket.connect(('199.1.8.41',80))#连接ip
print('..............已连接..................')
#客户端发送数据
info=''
while info!='q':
    #准备发送的数量
    send_data=input("请输入要发送的数据退了请输入q:")
    clinet_socket.send(send_data.encode('utf-8'))
    if send_data=='q':
        break
    #从服务器端接收数据
    info=clinet_socket.recv(1024).decode('utf-8')
    print('收到的数据：',info)
clinet_socket.close()#关闭对象

