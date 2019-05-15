#request response cycle

#port 80 is http
#port 443 is https
import socket
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    #connection point in my computer not yet connected to web
mysock.connect(('data.pr4e.org',80))        #(host,port) we want to connect to
#its like dialling the phone tohost site at port 
#cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)     #receive upto 512 characters
    if(len(data) < 1):
        break
    print(data.decode())
mysock.close()