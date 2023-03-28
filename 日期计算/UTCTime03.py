import datetime
import time

import pytz

# 获取当前本地时间
nYear = int(time.strftime('%Y', time.localtime(time.time())))
nMonth = int(time.strftime('%m', time.localtime(time.time())))
nDay = int(time.strftime('%d', time.localtime(time.time())))

local_time = datetime.datetime(nYear, nMonth, nDay)

# 将本地时间转换为UTC时间
utc_timezone = pytz.timezone('UTC')
utc_time = local_time.astimezone(utc_timezone)

print(utc_time)