from multiprocessing import Process
from queue import Queue

if __name__ == '__main__':
    q=Queue(3)
    #向队列中添加元素
    q.put('hello')
    q.put('world')
    q.put('python')

    q.put('html',block=True,timeout=2)#等2秒后还没有空位置就抛出异常

