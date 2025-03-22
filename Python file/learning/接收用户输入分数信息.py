#接收用户输入分数信息
#要求：分数在0-100之间，输出成绩，如果成绩不在该范围抛出异常信息，提示分数必须在0-100之间
try:
    i = int(input('请输入成绩：'))
    if i>=0 and i<=100:
        print('成绩：', i)
    else:
        raise Exception('分数必须在0-100之间')
except Exception as a:
    print(a)