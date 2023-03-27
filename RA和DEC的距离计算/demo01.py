import math


def angular_distance(ra1, dec1, ra2, dec2):
    # 将角度转换为弧度
    def to_radians(degrees):
        return degrees * math.pi / 180.0

    ra1 = to_radians(ra1)
    dec1 = to_radians(dec1)
    ra2 = to_radians(ra2)
    dec2 = to_radians(dec2)

    # 计算角距离
    cos_angle = math.sin(dec1) * math.sin(dec2) + math.cos(dec1) * math.cos(dec2) * math.cos(ra1 - ra2)
    angle = math.acos(cos_angle)

    # 将弧度转换为度数
    return math.degrees(angle)

distance = angular_distance(10, 10, 100, 20)
print(distance)