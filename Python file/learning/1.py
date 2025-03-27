class person():
    def eat(self):
        print('人，吃五谷杂粮')
class cat():
    def eat(self):
        print('猫，吃猫粮')
class dog:
    def eat(self):
        print('狗，吃骨头')
#这个三个都是一个共同点有一个同名的方法

#编写函数
def fun(obj):#obj形参
    obj.eat()#通过obj调用eat方法

#创建三个类的对象
per=person()
cat=cat()
dog=dog()

#调用fun函数
fun(per)#这就是python当中的多态，不关心你的对象数据类型，只关心你这个对象是否具有同名的方法
fun(cat)
fun(dog)


