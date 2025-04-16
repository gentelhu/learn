import pdfplumber
# 打开pdf文件
with pdfplumber.open('F:/gentel/learn/LiuYao/已整理/朱辰彬内部讲座六爻实战古筮真诠实战.pdf') as pdf:
    # 遍历页
    for page_num, page in enumerate(pdf.pages, start=1):
        # 只处理330页之后的内容
        if page_num > 330:
            # 提取当前页的文本
            text = page.extract_text()
            if text:
                lines = text.split('\n')
                for line in lines:
                    # 简单处理缩进，这里假设缩进是4个空格
                    if line.startswith(' ' * 4):
                        new_line = line
                    else:
                        new_line = line
            print(text)


