from queue import Queue
from threading import Thread
import time

from jinja2.utils import consume


#创建一个生产者类
class producar(Thread):
    def __init__(self,name,queue):
        Thread.__init__(self,name=name)
        self.queue=queue
    def run(self):
        for i in range(1,5):
            print(f'{self.name}的产品{i}放入队列')
            self.queue.put(i)
            time.sleep(1)
        print('生产者完成了所有数据的库放')

#创建一个消费者类
class Consumer(Thread):
    def __init__(self,name,queue):
        Thread.__init__(self,name=name)
        self.queue=queue
    def run(self):
        for _ in range(1,5):
            value=self.queue.get()
            print(f'消费者线程:{self.name}取出了{value}')
            time.sleep(1)
        print('..........消费者线程完成了把有数据的取出........')
if __name__ == '__main__':
    #创建队列
    queue=Queue()
    #创建生产者线程
    p=producar('producar',queue)
    #创建消费者线程
    c=Consumer('Consumer',queue)
    #启动线程
    p.start()
    c.start()
    #
    p.join()
    c.join()
    print('主线程执行结束')


