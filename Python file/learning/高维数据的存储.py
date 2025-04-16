import json
#准备数据
lst=[
    {'name':'gentel','age':20,'score':90},
    {'name':'tom','age':21,'score':99},
    {'name':'jeke','age':19,'score':89}
]
print(lst)
#编码
s=json.dumps(lst,ensure_ascii=False,indent=4)#ensure_ascii=False正常显示为中文、indent=4增加数据的缩进使json格式的字符串更有可读性
print(type(s))#编码的过程，将字典转成了字符串类型
print(s)
#解码
lst2=json.loads(s)
print(type(lst2))
print(lst2)

#编码到文件中
with open('txt/高维数据的存储.txt','w') as file:
    json.dump(lst,file,ensure_ascii=False,indent=4)

#解码到程序
with open('txt/高维数据的存储.txt','r') as file:
    lst3=json.load(file)
    print(type(lst3))
    print(lst3)