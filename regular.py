import re, math


def ret(str):
    ret = re.match("[0-9]{0,4},[0-9]{0,4},[0-9]{0,4},[0-9]{0,4},[0-9]{0,4}",str)
    if ret == None:
        return False
    else:
        return True

def group(str):
    ret = re.match("[0-9]{0,4},[[0-9]{0,4},[0-9]{0,4},[0-9]{0,4},[0-9]{0,4}",str)
    return ret.group()


def transfer(str):
    a = [int(i) for i in str.split(",")]
    return a

def final(data):
    '''
    :param data:CO2、甲醛、湿度、温度、PM2.5
    :return:
    '''
    record = ['', '', '', '', '',]
    index = transfer(group(data))
    record[0] = round((index[3]-500)/10)
    record[1] = round(index[2]/10)
    record[2] = index[0]
    record[3] = round(index[1]/100.00*1.34, 2)
    record[4] = index[4]
    return record


# def percent(index):
#     '''
#     max = [1000, 0.8, 100, 90, 250]
#     :param index:CO2、甲醛、湿度、温度、PM2.5
#     :return:
#     '''
#     percent = []
#     percent.append(round((index[0] + 20) * 1.25))
#     percent.append(index[1])
#     percent.append(round(index[2] / 10))
#     percent.append(round(index[3] * 125))
#     percent.append(round(index[4] / 2.5))
#     for i in range(5):
#         if percent[i] > 100:
#             percent[i] = 100
#     return percent


def percent(index):
    '''
    max = [1000, 0.8, 100, 90, 250]
    :param index:CO2、甲醛、湿度、温度、PM2.5
    :return:
    '''
    percent = []
    data = ['', '', '', '', '']
    percent.append(round((index[0] + 20) * 1.25))
    percent.append(index[1])
    percent.append(round(index[2] / 10))
    percent.append(round(index[3] * 125))
    percent.append(round(index[4] / 2.5))
    for i in range(5):
        data[i] = str(percent[i]) + r"%;"
        if percent[i] > 100:
            percent[i] = 100
            data[i] = str(percent[i]) + r"%; color: red;"
    return data


if __name__ == '__main__':
    a = "350,173,420,700,172"
    print(final(a))

"""
35.197.19.238
POST /figure HTTP/1.1
Host:192.168.1.110
Connection: Keep-Alive
Content-Length: 100
Content-Type:application/x-www-form-urlencoded

before=150,120,420,700,172&after=150,5,680,700,172


POST /figure HTTP/1.1
Host:35.197.19.238
Connection: Keep-Alive
Content-Length: 100
Content-Type:application/x-www-form-urlencoded

before=150,120,420,700,172&after=150,5,680,700,172
"""