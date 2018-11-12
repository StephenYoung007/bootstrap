import time
import pymongo
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

PORT = 8080

client=pymongo.MongoClient("localhost", 27017)

db=client['stephen']
mycol = db['test']
ori = {
    'name': 'test',
    'data': '27017'
}

def find(data):
    myquery = {'name': 'test'}
    back =  mycol.find(myquery)
    return back[0][data]

def insert(name, data):
    myquery = {'name': 'test'}
    newvalues_set = {"$set": {name: data}}
    mycol.update_one(myquery, newvalues_set)

if __name__ == '__main__':
    # before = find("before")
    # print(before)
    # s.bind(('', PORT))
    mycol.insert_one(ori)
    name = ["温度", "湿度", "CO2", "甲醛", "PM2.5"]
    insert("index", name)
    # # while True:
    # #     data, address = s.recvfrom(65535)
    # #     data = data.decode('utf-8')
    # myquery = {'name': 'test'}
    # #     print(data,'data')
    # newvalues_set = {"$set": {"data": 'hshsh'}}
    # mycol.update_one(myquery, newvalues_set)
    #     value = list(mycol.find(myquery))
    #     print(value)

# b = find()
# print(list(b)[0]['data'])
