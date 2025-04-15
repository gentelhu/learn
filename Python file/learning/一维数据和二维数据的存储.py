#一维数据的写入和读取，注意的是写入需要转换，读取需要转换
def my_write():
    #一维数据，可以使用列表，元组，集合
    lst=['张三','李四','王五']
    with open('excel/lst.csv','w',encoding='utf-8') as file:
        file.write(','.join(lst))#列表写不进去，只有转成字符串才能写进去
def my_read():
    with open('excel/lst.csv','r',encoding='utf-8') as file:
        s=file.read()
        lst=s.split(',')#将字符串转成列表
        print(lst)

#二维数据
def my_write_table():
    lst=[
        ['商品名称','单价','采购数量'],
        ['水杯','98.5','20'],#写入的数据要求都是字符串类型
        ['鼠标', '89', '100'],
    ]
    with open('excel/table.csv','w',encoding='utf-8') as file:
        for item in lst:
            line=','.join(item)
            file.write(line)
            file.write('\n')
def my_read_table():
    date=[]
    with open('excel/table.csv','r',encoding='utf-8') as file:
        lst=file.readlines()#读取的是每一行，是列表中的元素
        # print(type(lst),lst)
        for item in lst:
            new_lst=item[:len(item)-1].split(',')
            date.append(new_lst)
        print(date)

if __name__ == '__main__':
    # my_write()
    # my_read():
    # my_write_table()
    my_read_table()
