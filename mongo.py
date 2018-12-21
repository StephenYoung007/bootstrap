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
    'name': 17017,
    'data': '27017'
}

def find_(id, data):
    myquery = {"id": id}
    back =  mycol.find(myquery)
    # return back[0][data]
    li = list(back)[0][data]
    del li[2]
    return li

def findOrigin(id, data):
    myquery = {"id": id}
    back =  mycol.find(myquery)
    # return back[0][data]
    li = list(back)[0][data]
    # del li[2]
    return li

def insert_(id, name, data):
    myquery = {'id': id}
    newvalues_set = {"$set": {name: data}}
    mycol.update_one(myquery, newvalues_set)

def insert_new(id):
    myquery = {
        "id" : id,
    }
    myCursor = mycol.find(myquery)
    if myCursor.count() == 0:
        mycol.insert(myquery)
    name = ["温度", "湿度", "CO2", "甲醛", "PM2.5"]
    insert_(id, "index", name)


if __name__ == '__main__':
    # before = find("before")
    # print(before)
    # s.bind(('', PORT))
    # insert_new(17018)
    print(type(find_(17017, "percent_before")))
    # mycol.insert_one(ori)
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
