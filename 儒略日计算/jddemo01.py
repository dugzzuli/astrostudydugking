from astropy.time import Time

# 给定UT时间
ut_time = "2023-03-25T17:39:42"

# 创建Astropy的Time对象
t = Time(ut_time, format="isot", scale="utc")

# 获取儒略日
julian_day = t.jd


print("给定UT时间 %s 的儒略日为: %.5f" % (ut_time, julian_day))


