from astropy.time import Time

# 获取当前UTC时间
current_time_utc = Time.now()

# 将UTC时间转换为儒略日
julian_day = current_time_utc.jd

print("当前时刻的儒略日为:", julian_day)