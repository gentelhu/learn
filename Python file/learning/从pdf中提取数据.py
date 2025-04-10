import pdfplumber
#打开pdf文件
with pdfplumber.open('Python From Beginner to Expert.pdf') as pdf:#重命名为pdf
    for page_num, page in enumerate(pdf.pages, start=1):#遍历页enumerate函数会给pdf.pages中的每个元素配上一个序号，start=1表示序号从 1 开始
        if page_num > 2:#显示两页
            break
        print(page.extract_text())#extract_text()方法提取内容
        print(f'.............{page_num}页')
