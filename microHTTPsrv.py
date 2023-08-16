# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 09:55:16 2023

@author: Lucie
"""

import time
import socket

#TCP_IP = '10.9.127.207'
TCP_IP = '127.0.0.1'
TCP_PORT = 55000
BUFFER_SIZE = 1024 


#%% Fabien est le plus fort !

http = b"HTTP/1.1 200 OK\n\
Date: Sun, 29 Mar 2015 10:48:13 GMT\n\
Expires: -1\n\
Cache-Control: private, max-age=0\n\
Content-Type: text/html;\n\
charset=ISO-8859-1\n\n"
html= b"<html><body><h1>Fabien c'est le  plus fort</h1>\
</body></html>\n\n"

http_response = http+html

#%% In43 is the best course !

http_head = "HTTP/1.1 200 OK\r\n"
http_head += "Date:"+ time.asctime() +"GMT\r\n"
http_head += "Expires: -1\r\n"
http_head += "Cache-Control: private, max-age=0\r\n"
http_head += "Content-Type: text/html;"
http_head += "charset=utf-8\r\n"
http_head += "\r\n"
data = "<html><head><meta charset='utf-8'/></head>"
data += "<body><h1>In43 is the best course ! </h1>"
data += "</body></html>\r\n"
data += "\r\n"
http_response = http_head.encode("ascii") + data.encode("utf-8")

#%%

sconn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("binding to "+ TCP_IP +":"+str(TCP_PORT)," ...")
sconn.bind((TCP_IP, TCP_PORT))

print("Waiting client ...")
sconn.listen(1)

while True:
    s, addr = sconn.accept()
    print('Client connected with address:', addr)
    
    data = s.recv(BUFFER_SIZE) 
    s.send(http_response)  
    print('sending data...\n') 
    s.close()

print('Socket closed.')    
sconn.close()

