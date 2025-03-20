print("-"*10,"空心菱形图","-"*10)
#获取一个菱形的行数，因为菱形中间一行是分分割，所以只能是奇数
huoqu_lx=int(input("请输入菱形行数:"))
#如果用户输入的是奇数则要求重新输入
while huoqu_lx%2==0:
    print("输入错误请输入奇数")
    huoqu_lx = int(input("请输入菱形行数:"))
#菱形的上半部分
shang_hs=(huoqu_lx+1)//2
for i in range(1,shang_hs+1):
    for j in range(1,shang_hs+1-i):
        print(" ",end="")
    for k in range(1,i*2):
        if k==1 or k==i*2-1:
            print("*",end="")
        else:
            print(" ", end="")
    print()
#菱形的下半部分
for i in range(1,shang_hs):
    for j in range(1,i+1):
        print(" ", end="")
    for k in range(1,shang_hs*2-i*2): #531用range就是642
        if k == 1 or k == shang_hs*2-i*2-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

