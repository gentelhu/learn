#统计字符串中出现指定字符的次数
a='HelloPython,HelloJava,Hellophp'
# #用记用键盘录入 要查询的字符（不区分大小写),要求统计出要查找的字符在字符串中出现的次娄
# tongji=0
shuru=input('请输入一个需要查询的字符：')
# for item in range(len(a)):#方法1
#     if a[item].upper() == shuru.upper():
#         tongji += 1
# print(shuru,'出现次数是：',tongji)


#方法2

print('{0}在{1}出现了{2}次'.format(shuru,a,a.count(shuru.upper())))