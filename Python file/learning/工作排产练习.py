import openpyxl

# 加载工作簿
workbook = openpyxl.load_workbook('胎圈排产2025.4.9mm.xlsx')
# 获取指定工作表
sheet = workbook['PCM']
lst = []
# 遍历工作表的每一行
for row in sheet.rows:
    sublst = []
    # 遍历每行的每个单元格
    for cell in row:
        sublst.append(cell.value)
    lst.append(sublst)

# 根据条件追加数据
for item in lst:
    # 检查子列表的第二个元素是否为字符串，并且是否以 '08' 或 '09' 开头
    if isinstance(item[1], str) and (item[1].startswith('08') or item[1].startswith('09')):
        item.append('8#')
    elif isinstance(item[1], str) and (item[1].startswith('120') or item[1].startswith('121')):
        item.append('4#')
    elif isinstance(item[1], str) and (item[1].startswith('128') or item[1].startswith('129')):
        item.append('3#')
    elif isinstance(item[1], str) and (item[1].startswith('13') or item[1].startswith('14') or
                                       item[1].startswith('15') or item[1].startswith('16') or
                                       item[1].startswith('17')):
        item.append('5#')

# 创建新的工作表
sheet2 = workbook.create_sheet('排产')
# 向工作表中添加数据
for item in lst:
    sheet2.append(item)

# 保存修改后的工作簿
workbook.save('胎圈排产2025.4.9mm.xlsx')