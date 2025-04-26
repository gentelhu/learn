import threading
import time
from threading import Thread,Lock
ticket=50 #代表50张票
lock_obj=Lock()#创建锁对象

def sale_ticket(): #售票窗口
    global ticket
    for i in range(100):#相当于这个线程循环了100次
        lock_obj.acquire()#在判断之前上锁
        if ticket>0:
            print(f'{threading.current_thread().name}正在售票{ticket}张票')
            ticket-=1
        time.sleep(1)
        lock_obj.release()#使用完数据后解锁

if __name__ == '__main__':
    for i in range(3): #循环3次，内容创建三个线程，分别代表三个窗口
        t=Thread(target=sale_ticket)
        t.start()



