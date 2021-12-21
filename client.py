
import socket
from threading import Thread

from pymongo import MongoClient
import pymongo

client = pymongo.MongoClient("mongodb+srv://anuj:Anuj123@cluster0.fq5et.mongodb.net/test")
db = client["Chats"]

myCollection = db["chats"]

name = input("Enter your name: ")
client = ""


try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 5555))
    
    client.send(name.encode())
    


except Exception as e:
     for x in myCollection.find():
        dbName = x['name']
        dbChat = x['input']
        print(dbName, ":",dbChat)
    



def send(client):

    while True:

        try:
                   
            clientInput = input("")
            data = f'{name}:{clientInput}'
            client.send(data.encode())
            myDict = {"name" : name, "input" : clientInput}
            x = myCollection.insert_one(myDict)
        
        except Exception as e:

            pass
     

def receive(client):
    while True:
        try:
            data = client.recv(1024).decode()
            print(data)
        except Exception as e:
            client.close()
            break


thread1 = Thread(target=send, args=(client, ))
thread1.start()
thread2 = Thread(target=receive, args=(client, ))
thread2.start()

