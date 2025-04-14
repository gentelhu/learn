def my_read(filename):
    file=open(filename,'w+',encoding='utf-8')
    file.write('你好啊')#写入完成后文件的指针会在最后
    #读取文件，修改字针的位置
    file.seek(0)
    # s=file.read()#读取全部内部
    # s=file.read(2)#读取的是两个字符
    # s=file.readline()#读取一行
    # s=file.readline(2)#读取一行中的两个字符:你好
    # s=file.readlines()#读取所有内容，结果为列表类型:<class 'list'> ['你好啊']
    #调整文件指针位置
    file.seek(3)#指针移动到一个汉字以后，utf三个字节一个字
    s=file.read()#虽然是读取所有，但是把光标调整后把你的这个汉字给跳过了，只显示好啊
    print(type(s),s)
    file.close()
if __name__ == '__main__':
    my_read('txt/d.txt')

