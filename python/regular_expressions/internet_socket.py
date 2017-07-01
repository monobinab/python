#connect to web through sockets using 3 different techniques. 1. telnet 2. by python socket lib 3. by python urllib lib.
#go to command line and use telnet
telnet www.py4inf.com 80
GET hhtp://www.py4inf.com/code/romeo.txt HTTP/1.0 # then 2 times hit enter

###########################################################
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))

mysock.send('GET hhtp://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if (len(data) < 1) :
        break
    print data
mysock.close()

######################################################
# with urllib, it is like opening a file and reading from file

import urllib
fhand = urllib.urlopen('http://py4inf.com/code/romeo.txt')

for line in fhand:
    print line.strip()

#########################################################################
#home work assignment
telnet www.pythonlearn.com 80
GET http://www.pythonlearn.com/code/intro-short.txt/1.0


import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('pythonlearn.com', 80))
mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data;

mysock.close()