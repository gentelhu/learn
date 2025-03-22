from dis import print_instructions

lis=[['01','电风扇','美的',500],
    ['02','洗衣机','TCL',1000],
    ['03','微波炉','老板',400]
]
#格式化
print("编号\t\t\t商品\t\t\t品牌\t\t单价")
for i in lis:
    i[0] = '0000' + i[0]
    i[3] = '￥{0:,.2f}'.format(i[3])

for item in lis:
    for i in item:
        print(i,end="\t\t")
    print()


