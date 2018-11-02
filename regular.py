import re, math


def ret(str):
    ret = re.match("[1-9][0-9]{0,3},[1-9][0-9]{0,3},[1-9][0-9]{0,3},[1-9][0-9]{0,3},[1-9][0-9]{0,3}",str)
    if ret == None:
        return False
    else:
        return True

def group(str):
    ret = re.match("[1-9][0-9]{0,3},[1-9][0-9]{0,3},[1-9][0-9]{0,3},[1-9][0-9]{0,3},[1-9][0-9]{0,3}",str)
    return ret.group()


def transfer(str):
    a = [int(i) for i in str.split(",")]
    return a

def final(data):
    '''
    :param data:CO2、甲醛、湿度、温度、PM2.5
    :return:
    '''
    index = transfer(group(data))
    index[1] = round(index[1]/100.00*1.34, 2)
    index[2] = round(index[2]/10)
    index[3] = round((index[3]-500)/10)
    return index


def percent(index):
    '''
    max = [1000, 0.8, 100, 90, 250]
    :param index:
    :return:
    '''
    percent = []
    percent.append(round(index[0] / 10))
    percent.append(round(index[1] * 125))
    percent.append(index[2])
    percent.append(round((index[3] + 20) * 1.25))
    percent.append(round(index[4] / 2.5))
    for i in range(5):
        if percent[i] > 100:
            percent[i] = 100
    return percent


if __name__ == '__main__':
    a = "350,173,420,700,172"
    print(final(a))

"""
POST /figure HTTP/1.1
Host:192.168.1.110
Connection: Keep-Alive
Content-Length: 100
Content-Type:application/x-www-form-urlencoded

before=150,120,420,700,172&after=150,5,680,700,172
"""