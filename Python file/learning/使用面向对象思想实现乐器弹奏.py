#使用面向对象思想实现乐器弹奏
class instrument:
    def make_sound(self):
        pass
class erhu(instrument):
    def make_sound(self):
        print('二胡在演奏')
class piano(instrument):
    def make_sound(self):
        print('钢琴在演奏')
class violin(instrument):
    def make_sound(self):
        print('小提琴在演奏')
#定义一个函数弹奏各种乐器
def play(obj):
    obj.make_sound()
#测试
erhu=erhu()
piano=piano()
violin=violin()
#调用
play(erhu)
play(piano)
play(violin)