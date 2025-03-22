lst=[
    ["城市","环比","对比"],
    ['北京',102,103],
    ['上海',104,504],
    ['深圳',100,39]
]
print(lst)
for row in lst:
    for item in row:
        print(item,end="\t")
    print()

# 用列表生成式生成一个4行5列的列表
lst2=[[j for j in range(5)]for i in range(4)]
print(lst2)

for i in lst2:
    for y in i:
        print(y,end="\t\t")
    print()


