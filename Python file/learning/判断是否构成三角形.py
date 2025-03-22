try:
    a=int(input('请输入边长：'))
    b=int(input('请输入边长：'))
    c=int(input('请输入边长：'))
    if a==b==c:
        print(f'你分别输入的{a},{b},{c}是等边三角形')
    elif a+b>c and a+c>b and b+c>a:
        print(f'你分别输入的{a},{b},{c}是三角形')
    else:
        raise Exception(f'你分别输入的{a},{b},{c}不是三角形')
except Exception as a:
    print(a)