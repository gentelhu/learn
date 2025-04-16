import pandas as pd
import matplotlib.pyplot as plt
#读取excel文件
df=pd.read_excel('excel/JQ手机销售数据.xlsx')
print(df)
#绘图会产生中中文乱码，所以先解决中文乱码的问题，
plt.rcParams['font.sans-serif'] = ['SimSun']
#绘图需要设置画布的大小
plt.figure(figsize=(10,6))
labels=df['商品名称']
y=df['苏州出库量']
# print(labels)
# print(y)
plt.pie(y,labels=labels,autopct='%1.1f%%',startangle=90)
# #设置一下x,y轴一致，保证饼图是正圆
plt.axis('equal')
plt.title('2025年4月苏州各手机品牌出库量占比图')
# #显示图表
plt.show()