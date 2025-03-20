lis=['京A0000','沪A8888','苏A6666']
for i in lis:
    if i[0:1]=='京':
        print(i,'归属地是：北京')
    if i[0:1] == '沪':
        print(i, '归属地是：上海')
    if i[0:1] == '苏':
        print(i, '归属地是：苏州')
