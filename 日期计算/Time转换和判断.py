from datetime import datetime

def is_time_format(input_string):
    formats = ['%Y-%m-%d', '%Y-%m-%dT%H:%M:%S', '%Y-%m-%dT%H:%M:%S.%f', '%Y/%m/%d']
    for format in formats:
        try:
            datetime.strptime(input_string, format)
            return True
        except ValueError:
            pass
    return False

def convert_to_datetime(input_string):
    if is_time_format(input_string):
        formats = ['%Y-%m-%d', '%Y-%m-%dT%H:%M:%S', '%Y-%m-%dT%H:%M:%S.%f', '%Y/%m/%d']
        for format in formats:
            try:
                return datetime.strptime(input_string, format)
            except ValueError:
                pass
    return None

# 测试代码
input_string = '2023-03-27T12:38:59.999'
dt = convert_to_datetime(input_string)
if dt:
    print(dt.strftime('%Y-%m-%d %H:%M:%S'))
else:
    print('输入的字符串不是时间格式')