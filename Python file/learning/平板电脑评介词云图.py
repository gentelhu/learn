from traceback import print_tb
import jieba
from wordcloud import WordCloud
with open('txt/京东iPad 11英寸 A16芯片2025年款用户评价.txt','r',encoding='utf-8') as file:
    s=file.read()
#中文分词
lst=jieba.lcut(s)
#排除一些不好的词
stopword=['运行','散热','2025','03', '轻薄', '运行速度','流畅','屏幕效果','外观材质', '轻薄程度' ,
          '音质音效','屏幕清晰','系统流畅','其他特色']
txt=''.join(lst)
#绘制词云图
wordcloud=WordCloud(background_color='white',font_path='msyh.ttc',stopwords=stopword,
                    width=800,height=600)
#txt生成词云图
wordcloud.generate(txt)
#保存图片
wordcloud.to_file('image/ipad评价词云图.png')
