import numpy as np
import matplotlib.pyplot as plt#
#读取图片
m1=plt.imread('google.png')#数据是三维数据，分别是宽，高 RGB颜色
# print(m1)
plt.imshow(m1)
#灰度处理
m2=np.array([0.299,0.587,0.114])#创建灰度的数组
# 将数组mi和m2进行数组的点乘运算
x=np.dot(m1,m2)
# 传入数组
plt.imshow(x,cmap='gray')
# 显示图片
plt.show()


