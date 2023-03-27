from astropy import units as u
from astropy.coordinates import SkyCoord

# 定义第一个点
point1 = SkyCoord(ra=10*u.degree, dec=10*u.degree)

# 定义第二个点
point2 = SkyCoord(ra=100.0*u.degree, dec=20.0*u.degree)

# 计算两个点之间的角距离
angular_distance = point1.separation(point2)

# 将角距离转换为弧度并输出结果
print(angular_distance.deg)
print(angular_distance)