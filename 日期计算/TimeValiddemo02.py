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

# 测试代码
input_string = '2023-03-27'
if is_time_format(input_string):
    print('输入的字符串是时间格式')
else:
    print('输入的字符串不是时间格式')