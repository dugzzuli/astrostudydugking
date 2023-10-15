from astropy import units as u
from astropy.coordinates import SkyCoord
import datetime

def calc_distance(ra1, dec1, ra2, dec2, ra_unit='degree', dec_unit='degree', target_time=None):
    """
    计算赤道坐标间的角距离

    参数:
    - ra1 (float): 第一个坐标的赤经
    - dec1 (float): 第一个坐标的赤纬
    - ra2 (str): 第二个坐标的赤经，格式为 "HH:MM:SS.S" （时分秒用冒号分隔）
    - dec2 (str): 第二个坐标的赤纬，格式为 "+DD:MM:SS.S" 或 "-DD:MM:SS.S" （符号、度分秒用冒号分隔）
    - ra_unit (str): 第一个坐标的赤经单位，默认为 "degree"
    - dec_unit (str): 第一个坐标的赤纬单位，默认为 "degree"
    - target_time (str): 需要考虑天体历元的变化时指定目标时间（默认为 None）

    返回值:
    - distance (float): 两个坐标之间的角距离，单位为 "degree"
    """

    # 将赤经和赤纬转换为 Quantity 对象
    ra1 = ra1 * u.Unit(ra_unit)
    dec1 = dec1 * u.Unit(dec_unit)

    # 使用 SkyCoord 创建第一个坐标对象
    coord1 = SkyCoord(ra=ra1, dec=dec1, frame='icrs')

    # 使用 SkyCoord 创建第二个坐标对象，需要指定单位
    coord2 = SkyCoord(ra=ra2, dec=dec2, unit=(u.hourangle, u.deg), frame='icrs')

    # 考虑天体历元的变化（如果需要），可以通过 apply_space_motion 方法对坐标进行修正
    if target_time is not None:
        target_time = datetime.datetime.strptime(target_time, '%Y-%m-%d %H:%M:%S')
        coord2 = coord2.apply_space_motion(target_time=target_time)

    # 计算两个坐标之间的角距离
    sep = coord1.separation(coord2)

    # 返回结果
    return sep.degree

ra1 = 178.0
dec1 = 20.0
ra2 = '06:06:50.9'
dec2 = '+71:17:46'

distance = calc_distance(ra1, dec1, ra2, dec2, ra_unit='degree', dec_unit='degree')
print('距离为', distance, '度')