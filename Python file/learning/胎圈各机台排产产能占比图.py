from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType

list2 = [
    {"value": 417, "percent": 417 / 750},
    {"value": 2300, "percent": 2300 / 3111},
    {"value": 2370, "percent": 2370 / 3410},
    {"value": 1502, "percent": 1502 /2860},
    {"value": 3190, "percent": 3190 / 4000},
    {"value": 720, "percent": 720 / 1300},
]

list3 = [
    {"value": (750-417), "percent": (750-417)/ 750},
    {"value": (3111-2300), "percent": (3111-2300) / 3111},
    {"value": (3410-2370), "percent":  (3410-2370)/ 3410},
    {"value": (2860-1502), "percent": (2860-1502) /2860},
    {"value": (4000-3190), "percent": (4000-3190) / 4000},
    {"value": (1300-720), "percent": (1300-720) / 1300},
]

c = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis([1, 3, 4, 5, 6,8])
    .add_yaxis("当日排产", list2, stack="stack1", category_gap="50%")
    .add_yaxis("剩余产能", list3, stack="stack1", category_gap="50%")
    .set_series_opts(
        label_opts=opts.LabelOpts(
            position="right",
            formatter=JsCode(
                "function(x){return Number(x.data.percent * 100).toFixed() + '%';}"
            ),
        )
    )
    .render("html/胎圈各机台排产产能占比图.html")
)