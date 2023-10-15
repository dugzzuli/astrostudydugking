from astropy import units as u
from astropy.coordinates import SkyCoord
import datetime

ra = 178.0
dec = 20.0

ra_hms = '06:06:50.9'
dec_dms = '+71:17:46'

coord1 = SkyCoord(ra=ra*u.degree, dec=dec*u.degree, frame='icrs')
# 使用SkyCoord解析赤道坐标，参数中的u.degree表示单位为度，frame指定坐标系为ICRS

coord2 = SkyCoord(ra=ra_hms, dec=dec_dms,unit=('hourangle', 'deg'), frame='icrs')
# 同样通过SkyCoord解析第二组坐标


sep = coord1.separation(coord2)
# 计算两个坐标之间的角距离

print('距离为', sep.deg, '度')