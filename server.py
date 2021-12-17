import socket

from _thread import *
import threading

print_lock = threading.Lock()

def threaded(c):

  data = c.recv(1024)

  if not data:
    print("Bye")

    print_lock.release()

  data = data[::-1]

  c.send(data)

  c.close()

def Main():
  port = 12345

  s = socket.socket()
  s.bind(("", port))
  print("Socket binded to port", port)

  s.listen(5)

  
  print("Socket is listening")
  
  while True:

    c, addr = s.accept()

    print_lock.acquire()
    print("Connected to :", addr[0], ":", addr[1])

    start_new_thread(threaded, (c, ))
    
    
  s.close()


Main()

