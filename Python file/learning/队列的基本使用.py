from multiprocessing import Queue

if __name__ == '__main__':
    #创建一个队列
    q=Queue(3)#3表示最多可以接受3条信息
    print('队列是否为空',q.empty())
    print('队列是否为满',q.full())
    #向队列中添加消息
    q.put('hello')
    q.put('world')
    print('队列是否为空', q.empty())
    print('队列是否为满', q.full())
    q.put('python')
    print('队列是否为空', q.empty())
    print('队列是否为满', q.full())
    print('队列中有多少条消息',q.qsize())

    #出队
    print(q.get())
    print('队列中有多少条消息', q.qsize())
    #入队
    q.put_nowait('html')
    # q.put_nowait('sql')#输入这一条就报错了，因为队列已满，出了一个，入队两个
    # q.put('sql')#输入这个不会报错，但是处于等待中，等队列有空位，才可以添加进去
    #遍历队列中的元素
    if not q.empty():
        for i in range(q.qsize()):
            print(q.get_nowait())
    print('队列是否为空：',q.empty())
    print('队列是否为满：',q.full())
    print('队列中消息的个数：',q.qsize())

