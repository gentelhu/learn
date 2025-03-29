#算圆的面积和周长 面积的公式S=3.14*r的2次方  圆的周长公式C=2*3.14*r
class count():
    def __init__(self,r):
        self.r=r
    def s(self):
        return 3.14*pow(self.r,2)
    def c(self):
        return 2*3.14*self.r
r=eval(input("请输入圆的半径:"))
cou=count(r)
s=cou.s()
c=cou.c()
print(f"圆的面积：{s}\t圆的周长：{c}")
