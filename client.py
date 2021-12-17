# Import socket module
import socket
  
  
def Main():
    # local host IP '127.0.0.1'
    host = '127.0.0.1'
  
    # Define the port on which you want to connect
    port = 12345
  
    s = socket.socket()
  
    # connect to server on local computer
    s.connect((host,port))
  
    # message you send to server
    message = "My name is anuj kaushik"

  
        # message sent to server
    s.send(message.encode('ascii'))
  
        # messaga received from server
    data = s.recv(1024)
  
        # print the received message
        # here it would be a reverse of sent message
    print('Received from the server :',str(data.decode('ascii')))
  
        # ask the client whether he wants to continue
    
    
    s.close()
  

Main()