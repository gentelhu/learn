import socket
socket_obj=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#创建对象
socket_obj.bind(('199.1.8.41',80))#绑定ip
socket_obj.listen(5)#设置最大的连接数量
clinet_socket,clinet_addr=socket_obj.accept()#等待客户端的连接
print('服务器已启动等待连接')
#接收数据
info=clinet_socket.recv(1024).decode('utf-8')#初始化变量
while info!='q':#循环体
    if info!='':
        print('接收到的数据是：',info)
    #准备发送的数据
    data=input('请输入要发送的数据关闭通信请输入Q：')
    #服务器回复客户端
    clinet_socket.send(data.encode('utf-8'))
    if data.lower()=='q':
        break
    info = clinet_socket.recv(1024).decode('utf-8')#改变变量

#关闭socket对象
clinet_socket.close()
socket_obj.close()