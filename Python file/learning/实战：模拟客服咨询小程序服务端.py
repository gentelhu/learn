from socket import socket,AF_INET,SOCK_DGRAM
#1.创建socket对象
recv_socket=socket(AF_INET,SOCK_DGRAM)
#2.绑定IP和端口
recv_socket.bind(('199.1.8.41',666))
while True:
    #3.接收数据
    recv_data,addr=recv_socket.recvfrom(1024)
    print('客户说：',recv_data.decode('utf-8'))
    if recv_data.decode('utf-8')=='q':
        break
    #准备回得对方的信息
    data=input('回复信息：')
    #回复
    recv_socket.sendto(data.encode('utf-8'),addr)
#关闭
recv_socket.close()


