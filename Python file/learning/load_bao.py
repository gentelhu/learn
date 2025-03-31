import bao.mybao as my#导入包bao下面的mybao模块，并起别名叫my
my.info()

print('-'*60)
from bao import mybao as my #导入包名bao，下面的mybao模块并改别名为my
my.info()

print('-'*60)
from bao.mybao import info #导入bao名下mybao模块的info
info()#直接可以调用函数

print('-'*60)
from bao.mybao import * #用通配符导入
info()