# 计算不同类型图像的数目
```
SELECT imagetyp, COUNT(*)
FROM exposuresocs
WHERE obs_date BETWEEN '2023-03-25' AND '2023-03-26'
GROUP BY imagetyp;
```

# 计算每个类别，不同波段，不同曝光时间的统计
```
SELECT imagetyp,filter, exposure, COUNT(*) as count
FROM exposuresocs
WHERE imagetyp IN (
    SELECT DISTINCT imagetyp FROM exposuresocs WHERE obs_date BETWEEN '2023-03-25' AND '2023-03-26'
)
AND obs_date BETWEEN '2023-03-24' AND '2023-03-25'
GROUP BY imagetyp,filter, exposure;
```

#
```
SELECT imagetyp, exposure, COUNT(*) AS count
FROM exposuresocs
WHERE obs_date BETWEEN '2023-03-25' AND '2023-03-26'
GROUP BY imagetyp, exposure
```

# 使用mysql执行统计obs_date在20230325-20230326在之间，imagetyp='sc'，根据Object、filter、exposure分组
```
SELECT object, filter, exposure, COUNT(*) as count
FROM exposuresocs
WHERE obs_date BETWEEN '2023-03-25' AND '2023-03-26'
AND imagetyp='sc'
GROUP BY Object, filter, exposure;
```

