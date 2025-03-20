from enum import show_flag_values
class student:#创建了一个类
    school='北京大学'#这就是一个变量，类属性
    #实例属性
    def __init__(self,xm,age):#nm,age方法的参数，局部变量作用域只能在__init__内
        self.name=xm#等号的左侧是实例改属性，xm是局部变量,将局部变量的xm值赋值给了实例属性self.name
        self.age=age#实例属性的变量名称和局部变量的名称可以相同
    # 定义在类当中的函数就是实例方法
    def show(self):
        print(f'你的名字叫：{self.name}\t你的年龄：{self.age}')#self打点的实例属性可以在整个类中使用
#创建对象
stu1=student('gentel',40)
stu2=student('tom',28)
stu3=student('jimi',30)
#给类属性赋值
s=student.school='音乐学院'
print(s)
lis=[stu1,stu2,stu3]#列表当中的元素是student类型的对象
for item in lis:#item是列表当中的元素是student类型的对象
    item.show()#用对象名打点调用实例方法


