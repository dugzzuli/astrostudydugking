# 创建表，然后计算两个 ra和dec之间的距离
```sql
SELECT ra, decd,
    DEGREES(ACOS(
        SIN(RADIANS(decd)) * SIN(RADIANS(20.0)) +
        COS(RADIANS(decd)) * COS(RADIANS(20.0)) * COS(RADIANS(ra) - RADIANS(100.0))
    )) AS distance
FROM starsT;
```

# 同样的功能，计算两个 ra和dec之间的距离

```sql
SELECT 2 * ASIN(
    SQRT(
      POWER(SIN((RADIANS(10) - RADIANS(20)) / 2), 2) +
      COS(RADIANS(10)) * COS(RADIANS(20)) *
      POWER(SIN((RADIANS(100) - RADIANS(10)) / 2), 2)
    )
  ) * 180 / PI() as distance;

SELECT DEGREES(ACOS(SIN(RADIANS(dec1)) * SIN(RADIANS(dec2)) + COS(RADIANS(dec1)) * COS(RADIANS(dec2)) * COS(RADIANS(ra1 - ra2)))) AS distance
FROM (SELECT 10 AS ra1, 10 AS dec1, 100 AS ra2, 20 AS dec2) AS t;
```

# mysql数据库中创建函数进行调用，计算不同天文坐标（ra和dec）之间的距离
```sql
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
```



# 以下是一个示例SQL脚本，可以用于创建starsT表并向其中插入一些模拟数据：
```sql
CREATE TABLE starsT (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ra DECIMAL(10, 6),
    decd DECIMAL(10, 6)
);
INSERT INTO starsT (ra, decd) VALUES (10.123456, -45.678901);
INSERT INTO starsT (ra, decd) VALUES (20.234567, -35.789012);
INSERT INTO starsT (ra, decd) VALUES (30.345678, -25.890123);
INSERT INTO starsT (ra, decd) VALUES (40.456789, -15.901234);
INSERT INTO starsT (ra, decd) VALUES (50.567890, -5.912345);
INSERT INTO starsT (ra, decd) VALUES (60.678901, 4.076544);
INSERT INTO starsT (ra, decd) VALUES (70.790123, 14.065433);
INSERT INTO starsT (ra, decd) VALUES (80.901234, 24.054322);
INSERT INTO starsT (ra, decd) VALUES (91.012345, 34.043211);
INSERT INTO starsT (ra, decd) VALUES (101.123456, 44.032100);
```
这里的示例包含了一个名为starsT的表，其中包含3个列：id、ra和dec。id是自增的主键，ra和dec分别保存每个星体的赤经和赤纬。

该示例还向表中插入了10个具有不同RA和DEC值的数据点。您可以使用这些数据点来测试您的查询语句，例如：
```sql
SELECT ra, decd FROM starsT WHERE astronomical_distance(ra, decd, 60.0, 5.0) < 10.0;
```
这里的查询将返回距离(60.0, 5.0)小于10的所有行的RA和DEC值。请注意，在此示例中，distance()函数需要先在MySQL中定义，以便正确计算两个坐标之间的距离。




