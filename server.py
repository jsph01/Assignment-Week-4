import socket

s = socket.socket()
print ("Socket successfully created")

port = 9500

s.bind(('', port))
print ("socket binded to %s" %(port))

s.listen(5)
print ("socket is listening")

c, addr = s.accept()
print ('Got connection from', addr)

#if the client sends 'hi'
    #the server should send 'hello'
while True:
    msg = c.recv(1024).decode()

    if (msg == "Hello"):
        c.send("Hi".encode())
    else:
        c.send("Goodbye".encode())
        break
    

c.close()