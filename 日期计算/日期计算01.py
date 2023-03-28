from datetime import datetime, timedelta

# 获取当前日期和时间
now = datetime.now()

# 设置中午12点作为分界点
noon = datetime(now.year, now.month, now.day, 12)

# 判断当前时间与中午12点的关系
if now < noon:
    # 如果现在时间在中午12点前，则返回今天中午到明天中午的时间段
    start_time = datetime(now.year, now.month, now.day, 12)
    end_time = start_time + timedelta(days=1)
else:
    # 如果现在时间在中午12点后，则返回明天中午到后天中午的时间段
    start_time = datetime(now.year, now.month, now.day, 12) + timedelta(days=1)
    end_time = start_time + timedelta(days=1)

print(start_time)
print(end_time)