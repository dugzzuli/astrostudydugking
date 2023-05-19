# 计算不同类型图像的数目
SELECT imagetyp, COUNT(*)
FROM exposuresocs
WHERE obs_date BETWEEN '2023-03-25' AND '2023-03-26'
GROUP BY imagetyp;

# 计算每个类别，不同波段，不同曝光时间的统计
SELECT imagetyp,filter, exposure, COUNT(*) as count
FROM exposuresocs
WHERE imagetyp IN (
    SELECT DISTINCT imagetyp FROM exposuresocs WHERE obs_date BETWEEN '2023-03-25' AND '2023-03-26'
)
AND obs_date BETWEEN '2023-03-24' AND '2023-03-25'
GROUP BY imagetyp,filter, exposure;

#
SELECT imagetyp, exposure, COUNT(*) AS count
FROM exposuresocs
WHERE obs_date BETWEEN '2023-03-25' AND '2023-03-26'
GROUP BY imagetyp, exposure

# 使用mysql执行统计obs_date在20230325-20230326在之间，imagetyp='sc'，根据Object、filter、exposure分组
SELECT object, filter, exposure, COUNT(*) as count
FROM exposuresocs
WHERE obs_date BETWEEN '2023-03-25' AND '2023-03-26'
AND imagetyp='sc'
GROUP BY Object, filter, exposure;

#计算当前存在那些天
SELECT DATE(obs_date) AS date,
       imagetyp,
       COUNT(*) AS count
FROM exposuresocs
WHERE obs_date >= '2023-03-01'
  AND obs_date < DATE_ADD('2023-03-01', INTERVAL 1 MONTH)
GROUP BY DATE(obs_date), imagetyp;

SELECT DATE(obs_date) AS obs_date, imagetyp, COUNT(*) AS count
FROM exposuresocs
WHERE YEAR(obs_date) = YEAR(CURRENT_DATE()) AND MONTH(obs_date) = MONTH(CURRENT_DATE())
GROUP BY DATE(obs_date), imagetyp;