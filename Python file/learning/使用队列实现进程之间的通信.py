from multiprocessing import Queue,Process
import time

a=100
def write_msg(q): #q表示要操作的队列
    global a
    if not q.full():
        for i in range(6):
            a-=10
            q.put(a)
            print('a入队的值：',a)

def read_msg(q):
    time.sleep(1)
    while not q.empty():
        print('出队时a的值：',q.get(a))

if __name__ == '__main__':
    print('父进程开始执行')
    q=Queue()#同父进程创建队列，没有批定说明你指定的消息个数没有上限
    #创建两个进程一个负责入队一个负责出队
    p1=Process(target=write_msg(q,))
    p2=Process(target=read_msg(q,))
    #启动两个子进程
    p1.start()
    p2.start()
    #等待写的进程结束后，再去执行主进程
    p1.join()
    p2.join()
    print('...............父进程执行完毕..................')