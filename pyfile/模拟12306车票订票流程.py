che_c={
    'G1569':['北京南-天津南','18:06','18:39','00:33'],
    'G1567':['北京南-天津南','18:15','18:49','00:34'],
    'G8917':['北京南-天津西','18:20','19:19','00:59'],
    'G203':[' 北京南-天津南','18:35','19:09','00:34']
}
print('车次\t\t出发站-到达站\t\t出发时间\t\t到达时间\t\t历时时长')
for key in che_c.keys():
    print(key,end="   ")
    for item in che_c.get(key):
        print(item,end="\t\t")
    print()
che_m=input("请输入购票车次：")
info=che_c.get(che_m.upper(),"车次不存在")#info是一个列表类型
if info != "车次不存在":
    xingming=input("请输入乘车人，如果是多位乘车人使用逗号分号：")
    s=info[0]+' '+info[1]
    print("您已购买了"+che_m+" "+s+",请"+xingming.title()+'换取纸质车票。【铁路客服】')
else:
    print('对不起！选择的车次可能不存在')



