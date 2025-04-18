import os
# print("当前的工作路径",os.getcwd())
# print("当前路径下的所有目录及文件",os.listdir())
# print("指定的目录所有的文件",os.listdir('txt'))
#创建目录
# os.mkdir('case')#如果创建的文件夹存在程序报错
#创建多级目录
# os.makedirs('case/a/b')
#删除path下的空目录
# os.rmdir('case/a/b')
#删除多级目录
# os.removedirs('./case/a')
# 把path设置为当前目录
#os.chdir('txt')#改完成以，再写代码就是会时入txt这个文件夹
# 遍历目录树，结果为元组，包含所有路径名、所有目录列表和文件列表，相当于递归操作
# for dirs,dirlst,filelst in os.walk('F:/gentel/learn/system/Python file'):
#     print(dirs)
#     print(dirlst)
#     print(filelst)
#     print('*'*50)
#删除指定的文件
# os.remove('./AAA.py')
# 将old重名名为new
# os.rename('aaa.py','bbb.py')
# 获取path指定的文件信息,文件的操作时间信息，所以需要用时间函数翻译
import time
def date_format(longtiem):
    s=time.strftime('%Y-%m-%d',time.localtime(longtiem))
    return s

i=os.stat('./txt/京东iPad 11英寸 A16芯片2025年款用户评价.txt')
print(type(i),i)
print('最近的一次访问时间：',date_format(i.st_atime))
print('文件的创建时间：',date_format(i.st_ctime))
print('文件的大小：',i.st_size)

# 启动path指定的文件
# os.startfile('cmd.exe')#windows+r，输入命令可以找开的程序
#启动python.exe
os.startfile(r'C:\Users\KCP2110\AppData\Local\Programs\Python\Python313\python.exe')#\是python当中的提示符前面加个r让所有\提示符失效

