from datetime import datetime
from datetime import timedelta
#创建datetime的对象
delta=datetime(2020,10,1)-datetime(2020,5,1)#日期的运算
print(delta,type(delta))
print('2020年5月1号+delta天等于哪一天',datetime(2020,5,1)+delta)#

#通过一个参数创建timedelta对象
td1=timedelta(10,11)
print(td1)