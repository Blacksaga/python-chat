import socket

ser=socket.socket()
ser.bind(("192.168.43.221",3400))
print("server is started")
ser.listen()
print("server is wating for clinents request")
soc,caddr=ser.accept()
print("client is connected ")

while True:
    data=soc.recv(1024).decode("ascii")
    print("from client:",data)
    data=input()
    soc.send(data.encode("ascii"))
