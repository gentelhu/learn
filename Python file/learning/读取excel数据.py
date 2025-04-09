import openpyxl
workbook=openpyxl.load_workbook('景区天气.xlsx')
sheet=workbook['景区天气']
#景区数据是一个二维列表
lst=[]#存储行数数所
for row in sheet.rows:
    sublst=[]#存储单元格数据
    for cell in row:
        sublst.append(cell.value)
    lst.append(sublst)

for item in lst:
    print(item)

