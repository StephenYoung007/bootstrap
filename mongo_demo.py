import pymongo
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

PORT = 8080

client=pymongo.MongoClient("localhost", 27017)

db=client['demo']
mycol = db['test']
ori = {
    'name': 17017,
    'data': '27017'
}