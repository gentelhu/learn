import tkinter as tk
from calendar import monthcalendar
from lunardate import LunarDate
import datetime

def get_solar_term(year, month):
    # 简单获取节气的逻辑，实际可通过更专业库完善
    solar_terms = [
        "立春", "雨水", "惊蛰", "春分", "清明", "谷雨",
        "立夏", "小满", "芒种", "夏至", "小暑", "大暑",
        "立秋", "处暑", "白露", "秋分", "寒露", "霜降",
        "立冬", "小雪", "大雪", "冬至", "小寒", "大寒"
    ]
    days = [3, 18, 5, 20, 4, 19, 5, 21, 5, 21, 7, 23, 7, 23, 7, 23, 8, 23, 7, 22, 7, 22, 5, 20]
    base_date = datetime.date(year, 1, 1)
    offset = 0
    for i in range(month - 1):
        offset += days[i * 2]
    solar_term_date = base_date + datetime.timedelta(days=offset)
    return solar_term_date.strftime("%d") + "日 " + solar_terms[(month - 1) * 2]

def show_calendar(year, month):
    cal = monthcalendar(year, month)
    root = tk.Tk()
    root.title(f"{year}年{month}月日历")

    # 显示星期几
    weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    for col, weekday in enumerate(weekdays):
        label = tk.Label(root, text=weekday, relief=tk.RIDGE, width=10)
        label.grid(row=0, column=col)

    # 显示日期及相关信息
    for row_num, week in enumerate(cal, start=1):
        for col_num, day in enumerate(week):
            if day != 0:
                solar_date = datetime.date(year, month, day)
                lunar_date = LunarDate.fromSolarDate(solar_date.year, solar_date.month, solar_date.day)
                lunar_str = f"{lunar_date.month}月{lunar_date.day}日"
                label_text = f"{day}\n{lunar_str}"
                if month == 5 and (day == 5 or day == 21):  # 简单判断5月的立夏和小满节气
                    label_text += f"\n{get_solar_term(year, month)}"
                label = tk.Label(root, text=label_text, relief=tk.RIDGE, width=10)
                label.grid(row=row_num, column=col_num)

    root.mainloop()

if __name__ == "__main__":
    year = 2025
    month = 5
    show_calendar(year, month)