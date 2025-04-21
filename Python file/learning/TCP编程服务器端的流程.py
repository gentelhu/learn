from socket import socket,AF_INET,SOCK_STREAM
#AF_INET用于intelnet之间的进程通信
#SOCK_STREAM表示的是用TCP协议编程

#第一步创建socket对象
server_socket=socket(AF_INET,SOCK_STREAM)
#第二步绑定ip地址和端口号
ip='199.1.8.41'#本机的ip
port=80#自定义的端口
server_socket.bind((ip,port))#绑定了ip地址和端口号
#第三步开始TCP监听
server_socket.listen(5)#5代表排队数量
print('服务器已启动')
#第四步等等客户端的连接
client_socket,client_addr=server_socket.accept()#客户端的发送内容,系列解包赋值
#第五步接收来自客户端的数据
data=client_socket.recv(1024)#接收1024个数据
print('客户端发送过来的数据：',data.decode('utf-8'))#这里给date数据做了个转码，因为客户端发过来有编码
#第六步关闭socket
client_socket.close()
server_socket.close()




