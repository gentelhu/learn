from socket import socket,AF_INET,SOCK_DGRAM
send_socket=socket(AF_INET,SOCK_DGRAM)
#开始多次通信
while True:
    #准备发送的数据
    data=input('请输入发送信息输入q关闭通话：')
    #发送
    send_socket.sendto(data.encode('utf-8'),('199.1.8.41',8080))
    if data.lower()=='q':
        break
    #接收来自客服人员的回得信息
    recv_data,addr=send_socket.recvfrom(1024)
    print('客服说：',recv_data.decode('utf-8'))
#关闭
send_socket.close()
