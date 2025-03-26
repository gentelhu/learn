class person:#没有加（）默认是object的父类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f"大家好我叫：{self.name},我今年是{self.age}岁")

#接下来建立一个子类student去继承父类person
class student(person):#继承了父类拥有了当中公有的内容和受保护的东西
    def __init__(self,name,age,id):#name,age父类有可以继承，子类中新建了id
        super().__init__(name,age)#调用父类的初始化方法
        self.id=id
class doctor(person):#新建一个Doctor类
    def __init__(self,name,age,departmen):#建了一个部门的属性
        super().__init__(name,age)
        self.departmen=departmen

 #创建子类对象
stu=student('tom',20,'1001')
stu.show()
doc=doctor('gentel',30,'surgery')
#调用父类公有的方法
doc.show()










