#做一个偶数求和
a=int(input("请输入偶数求和的数字"))#定义变量
s=0#设定变量
i=1
for i in range(1,a+1):#判断条件
    if i%2==1:#语句块如果是奇数
        i += 1#执行i+1
        print(i)
        continue#不再执行后面的代码
    s+=i#改变变量
    i+=1
print(s)