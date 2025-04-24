import threading,time
from threading import Thread
class subThread(Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            print(f'线程：{threading.current_thread().name}正在执行{i}')

if __name__ == '__main__':
    print('主线程开始执行')
    lst = [subThread() for i in range(2)]
    for item in lst:#item的数据类型就是Thread类型
        #启动线程
        item.start()
    for item in lst:
        item.join()
    print(f'主线程执行完毕')
