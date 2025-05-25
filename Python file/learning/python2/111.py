class A:
    def __init__(self):
        print("A的构造方法")
    def say(self):
        print("A: ", self)
        print("say AAA")
class B(A):
    def __init__(self):
        super(B, self).__init__()  # 调用父类的构造方法
        print("B的构造方法")
    def say(self):
        # A.say(self)   调用父类的say方法
        super().say()  # 通过super()调用父类的方法
        print("say BBB")
b = B()
b.say()
