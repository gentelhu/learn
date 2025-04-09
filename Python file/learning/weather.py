import re
import requests

#定义函数
def get_html():

    ur='https://www.weather.com.cn/weather1d/101010100.shtml#search' #爬虫打开的浏览器上网的网做网页
    resp=requests.get(ur)#打开浏览器并打开网址
    resp.encoding='utf-8'#设置一下编码格式
    # print(resp.text)#响应对象
    return resp.text
def parse_html(html_str):
    #将上面所有的数据进行提取用正则表达式
    city=re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>',html_str,)
    weather=re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>',html_str,)
    wd=re.findall('<span class="wd">(.*)</span>',html_str,)
    zs=re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>',html_str,)
    #将数据打包
    lst=[]
    for a,b,c,d in zip(city,weather,wd,zs):
        lst.append([a,b,c,d])
    return lst