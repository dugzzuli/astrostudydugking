from datetime import datetime, timedelta

from loguru import logger


def getS_E_Time():
    # 获取当前日期和时间
    now = datetime.now()

    # 设置中午12点作为分界点
    noon = datetime(now.year, now.month, now.day, 12)

    # 判断当前时间与中午12点的关系
    if now < noon:
        start_time = datetime(now.year, now.month, now.day, 12)-timedelta(1)-timedelta(hours=8)
        end_time = noon-timedelta(8)
    else:
        # 如果现在时间在中午12点后，则返回今天中午12点到明天中午12点的时间段
        start_time = datetime(now.year, now.month, now.day, 12)-timedelta(hours=8)
        end_time = start_time + timedelta(days=1)-timedelta(hours=8)

    return start_time.strftime("%Y%m%d %H:%M"),end_time.strftime("%Y%m%d %H:%M")
if __name__ == '__main__':
    logger.info(getS_E_Time())
