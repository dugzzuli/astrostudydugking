from datetime import datetime

# 将字符串解析为datetime对象
dt = datetime.strptime("2022 11 26 172500", "%Y %m %d %H%M%S")

# 将datetime对象格式化为标准的日期时间字符串
formatted_dt = dt.strftime("%Y-%m-%d %H:%M:%S")

# 输出格式化后的结果
print(formatted_dt)