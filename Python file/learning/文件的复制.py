def copy(src,new_path):
    #文件的复制就是边读边写操作
    #打开源文件
    file1=open(src,'rb')
    #打开目标文件
    file2=open(new_path,'wb')
    #复制就是边读边写
    s=file1.read()#源文件读取所有
    file2.write(s)#新文件写入所有
    #关闭文档
    file2.close()#后打开的先关
    file1.close()#先打开的后关
if __name__ == '__main__':
    src='image/google.png'
    new_path='image/google副本.png'
    copy(src,new_path)
    print('文件复制完毕！')


