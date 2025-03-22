class student:
    def __init__(self,name,gender):
        self.name=name#普通属性
        self.__gender=gender#私有属性
    #用装饰器将方法转成属性@property,让他去修饰方法
    @property
    def gender(self):#通过调用他把属性数值转给私有属性
        return self.__gender#把属性当方法来使用，只能查看值不能修改值
    #将gender设置成可写属性
    @gender.setter#设置一个可写入方法
    def gender(self,value):
        if value!='men' and value!='wumen':
            print('性别有误，已将性别默认设置为women')
            self.__gender='women'
        else:
            self.__gender=value

stu=student('gentel','men')
# print(stu.gender)
print(stu.name,'性别是私有的无法访问但是可以访问方法',stu.gender)
#修改gender属性的值
stu.gender='other'
print(stu.gender)










