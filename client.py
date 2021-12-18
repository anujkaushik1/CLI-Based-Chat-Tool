
import socket
from threading import Thread

name = input("Enter your name: ")

print("Enter 1 to get all list of Rooms and 2 for creating new rooms")


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5555))

client.send(name.encode())



def receiveChatRoom(client):
    pass

def send(client):

    while True:

       data = f'{name}:{input("")}'
       client.send(data.encode())

    


def receive(client):
    while True:
        try:
            data = client.recv(1024).decode()
            print(data)
        except Exception as e:
            print(str(e))
            client.close()
            break


thread3 = Thread(target=receiveChatRoom, args=(client, ))
thread3.start
thread1 = Thread(target=send, args=(client, ))
thread1.start()
thread2 = Thread(target=receive, args=(client, ))
thread2.start()

