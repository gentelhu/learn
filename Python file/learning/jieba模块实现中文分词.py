import jieba
#读取文件
with open('txt/京东iPad 11英寸 A16芯片2025年款用户评价.txt','r',encoding='utf-8') as file:
    s=file.read()
# print(s)
#分词
lst=jieba.lcut(s)
# print(lst)
#去重操作
setl=set(lst)#用集合去重
#统计词出现的频率
d={}#使用字典的词，volue做为出现的频率
for item in setl:
    if len(item)>=2:
        d[item]=0
# print(d)
for item in lst:
    if item in d:
        d[item]=d.get(item)+1
# print(d)
new_lis=[]
for item in d:
    new_lis.append([item,d[item]])
# print(new_lis)

#列表排序
new_lis.sort(key=lambda x:x[1],reverse=True)
print(new_lis[0:11])#切片只显示前10项

