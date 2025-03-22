from sys import flags

print("模拟京东的购物流程")
lst=[]#存添加商品
for item in range(1001,1006):
    tianj_shangp=input("请输入你需要添加的商品：")
    lst.append(str(item)+tianj_shangp)
print("已经添加的商品信息：")
for item in lst:
    print(item)
lst2=[]#存购物车商品
while True:
    flag=False#代表没有商品的情况
    gouw_che=str(input("请输入你购买的商品编号退出请输入Q:"))
    for item in lst:
        if item[0:4]==gouw_che:
            flag=True
            lst2.append(item)
            print(item[4::],"添加购物车成功")
            break#退出了for循环
    if not flag and gouw_che.lower() !='q':#这里的not flag等于flag=false
        print("商品不存在")
    if gouw_che.lower()=='q':
        break
print("_"*50)
print("购物车的商品：")
lst2.reverse()
for item in lst2:
    print(item[4::])





