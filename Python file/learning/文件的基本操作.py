def my_write():
    #创建或找开文件
    file=open('txt/a.txt','w',encoding='utf-8')
    #写入文件
    file.write('伟大的中国梦')#写入字符
    #关闭文档
    file.close()
#读取
def my_read():
    # 创建或找开文件
    file = open('txt/a.txt', 'r', encoding='utf-8')
    #操作文件
    s=file.read()
    print(type(s),s)
    #关闭文件
    file.close()
#主程序运行
if __name__ == '__main__':
    # my_write()#调用函数
    my_read()
