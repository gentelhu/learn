print("-"*10,"用户登录系统","-"*10)#创建界面
i=0#定义变量
#登陆只有三次机会的系统
while i<3:
    mingzi=input("请输入用户名：")
    mima=input("请输入密码：")
    if mingzi=="guyue" and mima=="666666":
        print("系统正在登录中。。。")
        break
    else:
        if i<2:#第一次执行的是i=0,第二次是i=1,第三次不执行
            print("密码错误，你还有",2-i,"次机会！")
        i += 1#改变变量
if i==3:
    print("密码错误次数过多，请24小时后再次输入")



