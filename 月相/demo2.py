import ephem

# 创建观测者对象并设置经纬度、海拔高度、日期和时间
lijiang = ephem.Observer()
lijiang.lon, lijiang.lat = '100.03222222222', '26.69777'
lijiang.elevation = 3000
lijiang.date = '2023/3/25 10:16:09'

# 计算月亮在给定时间的位置
moon = ephem.Moon()
moon.compute(lijiang)

# 获取月相信息
phase_name = ephem.next_full_moon(lijiang.date)  # 下一个满月的日期和时间
illumination = moon.moon_phase  # 月亮照明率（0-1之间的值）
phase_angle = moon.phase

print(f"下一个满月是在 {phase_name}")
print(f"月亮照明率为 {illumination}")
print(f"月相为 {phase_angle}")