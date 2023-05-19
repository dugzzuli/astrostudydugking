from datetime import date, datetime, timedelta

def get_first_and_last_day_of_month():
    today = date.today()
    first_day_of_month = today.replace(day=1)
    last_day_of_month = today.replace(day=28) + timedelta(days=4) - timedelta(days=1)

    # 如果需要输出时分秒可以用下面两行替换第二行：
    # first_day_of_month = datetime(today.year, today.month, 1)
    # last_day_of_month = datetime(today.year, today.month, 1) + timedelta(days=32 - today.day) - timedelta(seconds=1)

    return (first_day_of_month, last_day_of_month)

# 调用函数并打印结果
(first_day, last_day) = get_first_and_last_day_of_month()
print("当前月的第一天：", first_day)
print("当前月的最后一天：", last_day)