from operator import itemgetter

import weather
import openpyxl
html=weather.get_html()#发送请求，得响应结果
lst=weather.parse_html(html)#解析数据
#创建一个新的excel工作薄
workbook=openpyxl.Workbook()#创建对象
#在excel当中去创建工作表
sheet=workbook.create_sheet('景区天气')
#向工作表中添加数据
for item in lst:
    sheet.append(item)#一次添加一行

workbook.save('景区天气.xlsx')

