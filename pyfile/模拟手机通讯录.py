tongxl=set()
for i in range(1,5):
    into=input(f'请输入第{i}位好友的姓名和手机号码：')
    tongxl.add(into)
print('已添加的号码')
for item in tongxl:
    print(item)
