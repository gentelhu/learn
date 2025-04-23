import os
import time
from multiprocessing import Process

#我的进程要执行的代码
def test():
    print(f'我是子进程，我的pip是：{os.getpid()},我的父进程是：{os.getppid()}')
    time.sleep(1)

if __name__ == '__main__':
    print('主进程开始执行')
    lis=[]
    #创建五个子进程
    for i in range(5):
        #创建子进程
        p=Process(target=test)
        #启动子进程
        p.start()
        #将启动中的进程加入列表当中
        lis.append(p)
    #遍历列表，lis中有个子进程，当子进程执行完毕后，再结束主进程
    for item in lis:
        item.join()#阻塞主进程
    print('主进程执行结束')