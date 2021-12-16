import socket 

s = socket.socket()

port = 12345
print("Socket Created Successfully")

s.bind(('', port))      
print("socket bounded to %s" %(port))

s.listen(5)
print("Socket is listening")



# Establish connection with client.
c, addr = s.accept()          #Accept a connection. The socket must be bound to an address and listening for connections. The return value is a pair (conn, address) where conn is a new socket object usable to send and receive data on the connection, and address is the address bound to the socket on the other end of the connection.
print ('Got connection from', addr )
  
  # send a thank you message to the client. encoding to send byte type.
c.send('Thank you for connecting'.encode())
 
  # Close the connection with the client
c.close()
   
  # Breaking once connection closed
