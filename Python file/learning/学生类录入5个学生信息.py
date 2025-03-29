from traceback import print_tb
class student:
    def __init__(self,name,age,genden,fraction):
        self.name=name
        self.age=age
        self.genden=genden
        self.fraction=fraction
    def info(self):
        print(self.name,self.age,self.genden,self.fraction)
lst=[]
print("请输入5位学生信息，（姓名#年龄#性别#成绩）")
for i in range(1,6):
    s=input(f"输入第{i}位学生信息：")
    s_lst=s.split('#')
    stu=student(s_lst[0],s_lst[1],s_lst[2],s_lst[3],)
    lst.append(stu)#这里将stu这个对象装进了lst这个列表里了
for item in lst:
    item.info()
