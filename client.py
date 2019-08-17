import socket

soc=socket.socket()
soc.connect(("DESKTOP-R59EFVA",3400))

while True:
     data=input()
     soc.send(data.encode("ascii")) 
     data=soc.recv(1024).decode("ascii")
     print("from client:",data)
    
