import re
import requests
ur='https://www.weather.com.cn/weather1d/101010100.shtml#search' #爬虫打开的浏览器上网的网做网页
resp=requests.get(ur)#打开浏览器并打开网址
resp.encoding='utf-8'#设置一下编码格式
# print(resp.text)#响应对象
#将上面所有的数据进行提取用正则表达式
city=re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>',resp.text,)
weather=re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>',resp.text,)
wd=re.findall('<span class="wd">(.*)</span>',resp.text,)
zs=re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>',resp.text,)
print(city)
print(weather)
print(wd)
print(zs)
#将数据打包
lst=[]
for a,b,c,d in zip(city,weather,wd,zs):
    lst.append([a,b,c,d])
for item in lst:
    print(item)
