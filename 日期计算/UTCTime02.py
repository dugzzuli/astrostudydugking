from datetime import datetime, timedelta
import pytz
def get_utc_time_and_day_range():
    # 获取当前时间
    local_time = datetime.now()

    # 将当前时间转换为UTC时间
    utc_time = local_time.astimezone(pytz.utc)

    # 计算当前一天的UTC0点到24点
    start_of_day_utc = datetime(utc_time.year, utc_time.month, utc_time.day, tzinfo=pytz.utc)
    end_of_day_utc = start_of_day_utc + timedelta(days=1)

    return utc_time, start_of_day_utc, end_of_day_utc

utc_time, start_of_day_utc, end_of_day_utc = get_utc_time_and_day_range()

print("当前UTC时间：", utc_time)
print("当前一天的UTC0点到24点：")
print(start_of_day_utc, "到", end_of_day_utc)