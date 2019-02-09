import socket

s = socket.socket()
port = 9500
s.connect (('127.0.0.1', port))

msg = "Hello"
while msg == "Hello":
    msg = input("Type in messsage to send to the server\n")
    s.send(msg.encode())
    print(s.recv(1024).decode())

s.close()