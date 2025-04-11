from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker
#准备数据
lst=[['化为', 1000], ['oppo', 1200], ['iphone', 300], ['mi', 980]]

c = (
    Pie()
    # .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
    .add("", lst)
    .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
    .set_global_opts(title_opts=opts.TitleOpts(title="2024年北京手机出库占比"))#标题
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("html/phone.html")#改文件名字
)

# print([list(z) for z in zip(Faker.choose(), Faker.values())])
