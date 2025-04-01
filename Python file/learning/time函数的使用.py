import time
now=time.time()
print(now)

obj=time.localtime()
print(obj)#对象可以看到看月日等全部信息

obj2=time.localtime(60)#60代表60秒
print(obj2)
print("year:",obj2.tm_year)

print(time.ctime())#易读的字符串
print(time.strftime('%Y年%m月%d日  %H：%M：%S',time.localtime()))#日期时间格式化
print(time.strptime('2008-8-8','%Y-%m-%d'))#将所提供的字符串转成对象
time.sleep(2)#程序暂停2秒
print('helloworld')