from socket import socket,AF_INET,SOCK_DGRAM
#一、create obj
send_socket=socket(AF_INET,SOCK_DGRAM)
#二、准备send data
data=input('请输入要发送的数据：')
#三、接收方ipAddress
ip_port=('199.1.8.41',80)
#四、send data
send_socket.sendto(data.encode('utf-8'),ip_port)
#五、接收方的回复数据
recv_data,addr=send_socket.recvfrom(1024)
print('接收到的数据为：',recv_data.decode('utf-8'))
#close socket
send_socket.close()



