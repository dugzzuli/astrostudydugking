from datetime import datetime

def is_time_format(input_string):
    try:
        datetime.strptime(input_string, '%Y-%m-%dT%H:%M:%S.%f')
        return True
    except ValueError:
        return False

# 测试代码
input_string = '2023-03-27'
if is_time_format(input_string):
    print('输入的字符串是时间格式')
else:
    print('输入的字符串不是时间格式')