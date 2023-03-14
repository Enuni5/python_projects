import socket

# simple web browser

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # stablish protocol to communicate
mysock.connect(('data.pr4e.org', 80)) # where to connect
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() # The request to the server
mysock.send(cmd) # Sending the request

while True:
    data = mysock.recv(512) # receiving data from the request
    if (len(data) < 1):
        break
    print(data.decode()) #parsing the data and printing it
mysock.close() # closing the connection