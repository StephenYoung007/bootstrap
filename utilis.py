import time


def format_time():
    format = '%Y-%m-%d %H:%M:%S'
    value = time.localtime(int(time.time()))
    return time.strftime(format, value)