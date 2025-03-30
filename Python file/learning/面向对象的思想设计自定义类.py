class vehicle:
    def __init__(self,model,license_plate):
        self.model=model
        self.license_plate=license_plate
    def start(self):
        print('启动')
    def stop(self):
        print('停止')

class taxi(vehicle):
    def __init__(self,model,license_plate,company):
        super().__init__(model,license_plate)
        self.company=company
    #重写父类方法
    def start(self):
        print(f'乘客你好我是{self.company}公司的，我的车牌是{self.license_plate},您要去哪里？')
    def stop(self):
        print('目的地快到了，请您付款下车，欢饮下次乘坐')
class family_car(vehicle):
    def __init__(self, model, license_plate, name):
        super().__init__(model, license_plate)
        self.name=name
        # 重写父类方法
    def start(self):
        print(f'我是{self.name},我的汽车我做主')
    def stop(self):
        print('目的地快到了我们去玩吧')

t=taxi('福克斯','京：888888','长城')
t.start()
t.stop()
f=family_car('byd','苏：666666','gentel')
f.start()
f.stop()
