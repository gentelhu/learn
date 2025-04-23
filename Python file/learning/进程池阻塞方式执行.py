from multiprocessing import Pool
import time,os
#编写函数
def task(name):
    print('子进程的pid',os.getpid(),'执行的任务',name)
    time.sleep(1)

if __name__ == '__main__':
    #主进程
    start=time.time()
    print('父进程开始执行')
    #创建进程池
    p=Pool(3)
    #创建任务
    for i in range(10):
        #以阻塞的方式执行
        p.apply(func=task,args=(i,))
    p.close()#关闭进程池
    p.join()#阻塞一下主进程，子进程结束以后才会执行父进程的代码
    print('所有的子进程执行完毕，父进程执行结束')
    print(int(time.time()-start),'秒')