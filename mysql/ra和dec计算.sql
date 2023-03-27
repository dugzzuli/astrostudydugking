# 创建表，然后计算两个 ra和dec之间的距离


SELECT ra, decd,
    DEGREES(ACOS(
        SIN(RADIANS(decd)) * SIN(RADIANS(20.0)) +
        COS(RADIANS(decd)) * COS(RADIANS(20.0)) * COS(RADIANS(ra) - RADIANS(100.0))
    )) AS distance
FROM starsT;

# 同样的功能，计算两个 ra和dec之间的距离
SELECT 2 * ASIN(
    SQRT(
      POWER(SIN((RADIANS(10) - RADIANS(20)) / 2), 2) +
      COS(RADIANS(10)) * COS(RADIANS(20)) *
      POWER(SIN((RADIANS(100) - RADIANS(10)) / 2), 2)
    )
  ) * 180 / PI() as distance;

SELECT DEGREES(ACOS(SIN(RADIANS(dec1)) * SIN(RADIANS(dec2)) + COS(RADIANS(dec1)) * COS(RADIANS(dec2)) * COS(RADIANS(ra1 - ra2)))) AS distance
FROM (SELECT 10 AS ra1, 10 AS dec1, 100 AS ra2, 20 AS dec2) AS t;


# mysql数据库中创建函数进行调用，计算不同天文坐标（ra和dec）之间的距离
CREATE FUNCTION astronomical_distance(ra1 FLOAT, dec1 FLOAT, ra2 FLOAT, dec2 FLOAT)
RETURNS FLOAT
DETERMINISTIC
READS SQL DATA
BEGIN
  DECLARE d_ra FLOAT;
  DECLARE d_dec FLOAT;
  DECLARE a FLOAT;
  DECLARE c FLOAT;

  -- 将RA和DEC转换为弧度
  SET ra1 = RADIANS(ra1);
  SET dec1 = RADIANS(dec1);
  SET ra2 = RADIANS(ra2);
  SET dec2 = RADIANS(dec2);

  -- 计算RA和DEC之间的差异
  SET d_ra = ra2 - ra1;
  SET d_dec = dec2 - dec1;

  -- 计算Haversine公式中的a和c
  SET a = SIN(d_dec / 2) * SIN(d_dec / 2) + COS(dec1) * COS(dec2) * SIN(d_ra / 2) * SIN(d_ra / 2);
  SET c = 2 * ATAN2(SQRT(a), SQRT(1 - a));

  -- 返回结果（以度为单位）
  RETURN c * 180 / PI();
END

SELECT astronomical_distance(10, 10, 100, 20) AS distance;