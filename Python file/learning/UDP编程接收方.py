from socket import socket,AF_INET,SOCK_DGRAM
#1.创建socket对象
recv_socket=socket(AF_INET,SOCK_DGRAM)
#2.绑定ip地址和端口
recv_socket.bind(('199.1.8.41',80))
#3.接收来自发送方的数据
recv_data,addr=recv_socket.recvfrom(1024)
print('接收到的数据为',recv_data.decode('utf-8'))
#4.准备回复对方的数据
data=input('请输入要回复的数据：')
#5.回复
recv_socket.sendto(data.encode('utf-8'),addr)
#6.关闭
recv_socket.close()

