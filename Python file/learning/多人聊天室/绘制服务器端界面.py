import wx
from socket import socket,AF_LINK,SOCK_STREAM
class gentelserver(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,id=1002,title='服务器端界面',pos=wx.DefaultPosition,size=(400,450))
        #创建面板
        pl=wx.Panel(self)
        #创建盒子
        box=wx.BoxSizer(wx.VERTICAL)#垂直方向自动排版
        #创建可伸缩的网格布局
        fgz1=wx.FlexGridSizer(wx.HSCROLL)#水平方向布局
        #创建三个按钮
        start_server_btn=wx.Button(pl, size=(133, 40), label='启动服务')
        record_btn=wx.Button(pl, size=(133, 40), label='保存聊天记录')
        stop_server_btn=wx.Button(pl, size=(133, 40), label='停止服务')
        #将三个按钮放到可伸缩网络中
        fgz1.Add(start_server_btn,1,wx.TOP)
        fgz1.Add(record_btn,1,wx.TOP)
        fgz1.Add(stop_server_btn,1,wx.TOP)
        #将可伸缩网络放入合子中
        box.Add(fgz1,1,wx.ALIGN_CENTRE)#居中对齐
        # 只读文本框，对于显示聊天内容
        self.show_text = wx.TextCtrl(pl, size=(400, 410), style=wx.TE_MULTILINE | wx.TE_READONLY)
        # 将文本框放入box中
        box.Add(self.show_text, 1, wx.ALIGN_CENTRE)
        #把盒子放到面板当中
        pl.SetSizer(box)
        '''...............以上是界面的绘制........................'''
        self.isOn=False #存储服务器的启动状态，默认没有启动
        # #设置服务器绑定的ip地址和端口号199.1.8.41
        self.host_port=('199.1.8.41',80)#空的字符串表示本机ip
        # #创建socket对象
        self.server_socket=socket(AF_LINK,SOCK_STREAM)
        #绑定ip和端口
        self.server_socket.bind(self.host_port)
        #开始监听
        self.server_socket.listen(5)
        #创建一个字典，与客户端对话的线程
        self.session_thread_dict={} #key -value,客户端的名称做为键，会话做为值

        #当属标点击启动的时候要执行的操作
        self.Bind(wx.EVT_BUTTON,self.start_server,start_server_btn)

    def start_server(self,event):
        print('启动服务的按钮被点击了')





if __name__ == '__main__':
    # 初始化app
    app = wx.App()
    # 创建自己的服务器端对象
    server = gentelserver()
    server.Show()  # 可以改成ysjclient('python娟子姐'.Show（)）
    # 循环刷新显示
    app.MainLoop()

