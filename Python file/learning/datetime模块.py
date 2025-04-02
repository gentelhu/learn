from datetime import datetime#从datetime模块中导入datetime类
dt=datetime.now()#获取当前系统的时间和时间
print(dt)
#datetime是一个类，手动创建这个类的对象
dt2=datetime(2020,8,8,20,8)
print(dt2,type(dt2))
print(dt2.year,dt2.month,dt2.day)#将dt2的年月日单独取出来

#比较datetime对象的大小
print(dt<dt2)

#datetiem类型与字符串转换
d3=dt.strftime('%Y %m %d')
print(d3,type(d3))

#将字符串类型转成datetiem类型
d4=datetime.strptime(d3,'%Y %m %d')
print(d4,type(d4))

print("*"*60)




