from datetime import datetime, timedelta

def get_first_and_last_day_of_month(date_str):
    date_obj = datetime.strptime(date_str, '%Y%m%d')
    first_day_of_month = date_obj.replace(day=1)
    last_day_of_month = first_day_of_month.replace(
        day=28) + timedelta(days=4) - timedelta(days=1)
    if last_day_of_month.month != first_day_of_month.month:
        last_day_of_month = first_day_of_month.replace(
            day=1) + timedelta(days=32 - first_day_of_month.day) - timedelta(days=1)
    return first_day_of_month.strftime('%Y-%m-%d'), last_day_of_month.strftime('%Y-%m-%d')

print(get_first_and_last_day_of_month('20230225'))