import os
import os.path

def mkdirs(path,num):
    for item in range(1,num+1):#批量创建
        os.mkdir(path+'/'+str(item))#他奸文件夹

if __name__ == '__main__':
    path='./mkdir'
    if not os.path.exists(path):
        os.mkdir(path)
    num=eval(input("请输入创建目录的个数："))
    mkdirs(path,num)


