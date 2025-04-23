from multiprocessing import Process
import os,time
#函数调用子进程
def sub_process(name):
    print(f'子进程的PID：{os.getpid()},父进程的PID：{os.getppid},..........{name}')
    time.sleep(1)
def sub_process2(name):
    print(f'子进程的PID：{os.getpid()},父进程的PID：{os.getppid},..........{name}')
    time.sleep(1)

if __name__ == '__main__':
    print('主进程开始执行')
    for i in range(5):
        p1=Process(target=sub_process,args=('jsy',))
        p2=Process(target=sub_process,args=(18,))

        p1.start()
        p2.start()

        #强制终止进程
        p1.terminate()#子进程刚开始就被结束了，所有没有了进程
        p2.terminate()
    print('主进程执行结束')
