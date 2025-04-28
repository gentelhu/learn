#coding:utf-8
import wx

class ysjclient(wx.Frame):
    def __init__(self, client_name):
        # 调用父类的初始化方法
        # None代表没有父级窗口
        # id自己定义的表示当前窗口的编号
        # 窗体的标题
        # pos窗体的打开位置，采用的默认
        # size窗体的大小，单位为像素400是宽度，450为高度
        wx.Frame.__init__(self, None, id=1001, title=client_name + '的客户端界面', pos=wx.DefaultPosition, size=(400, 450))
        # 创建面板对象
        pl = wx.Panel(self)
        # 面板上的盒子
        box = wx.BoxSizer(wx.VERTICAL)  # vertical垂直布局
        # 创建可伸缩的风格布局
        fqz1 = wx.FlexGridSizer(wx.HSCROLL)  # 水平方向布局
        # 创建两个按钮对象
        conn_btn = wx.Button(pl, size=(200, 40), label='连接')  # 按钮的大小
        dis_btn = wx.Button(pl, size=(200, 40), label='断开')  # 按钮的大小
        # 把两个按钮放到可伸缩网络布局中
        fqz1.Add(conn_btn, 1, wx.TOP | wx.LEFT)  # 顶部左对齐
        fqz1.Add(dis_btn, 1, wx.TOP | wx.RIGHT)  # 顶部右对齐
        # 将网格布局添加到box中
        box.Add(fqz1, 1, wx.ALIGN_CENTRE)  # wx.ALIGN_CENTRE居中对齐

        # 只读文本框，对于显示聊天内容
        self.show_text = wx.TextCtrl(pl, size=(400, 210), style=wx.TE_MULTILINE | wx.TE_READONLY)
        # 将文本框放入box中
        box.Add(self.show_text, 1, wx.ALIGN_CENTRE)

        # 创建聊天内容的文本框
        self.chat_text = wx.TextCtrl(pl, size=(400, 120), style=wx.TE_MULTILINE)
        # 将文本框放入box中
        box.Add(self.chat_text, 1, wx.ALIGN_CENTRE)

        # 创建可伸缩的风格布局
        fqz2 = wx.FlexGridSizer(wx.HSCROLL)  # 水平方向布局
        # 创建两个按钮对象
        reset_btn = wx.Button(pl, size=(200, 40), label='重置')  # 按钮的大小
        send_btn = wx.Button(pl, size=(200, 40), label='发送')  # 按钮的大小
        fqz2.Add(reset_btn, 1, wx.TOP | wx.LEFT)  # 顶部左对齐
        fqz2.Add(send_btn, 1, wx.TOP | wx.RIGHT)  # 顶部右对齐
        # 将网格布局添加到box中
        box.Add(fqz2, 1, wx.ALIGN_CENTRE)  # wx.ALIGN_CENTRE居中对齐

        # 将盒子放在面板中
        pl.SetSizer(box)


if __name__ == '__main__':
    # 初始化app
    app = wx.App()
    # 创建自己的客户端对象
    client = ysjclient('gentel')
    client.Show()  # 可以改成ysjclient('python娟子姐'.Show（)）
    # 循环刷新显示
    app.MainLoop()