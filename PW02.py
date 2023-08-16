# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 08:57:28 2023

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
import os
Path = "C:/Users/Lucie/Desktop/COURS/AERO4/S2/SYSTEME/RESEAUX/TP2/www"

sconn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("binding to "+ TCP_IP +":"+str(TCP_PORT)," ...")
sconn.bind((TCP_IP, TCP_PORT))

print("Waiting client ...")
sconn.listen(1)

dct = {"html":"text/html;charset=utf8","ico":"image/x-icon","jpg":"image/jpeg"}

while True:
    s, addr = sconn.accept()
    print('Client connected with address:', addr)
    
    data = s.recv(BUFFER_SIZE) 
    if data == 'exit':
        s.close()
        continue
    data_decoded = data.decode("ascii")
    print(data_decoded)

    data_request = data_decoded.split('\r\n')
    data_list = data_request[0].split(' ')
    method = data_list[0]
    #print(method)                  #to print the method
    data_ressource = data_list[1]
    #print(data_ressource,'\n')     #to print the ressource

    
    if method != "GET":
        http_head = "HTTP/1.1 405 Method not allowed \r\n\r\n"
        http_data = "<html><body><p>405 cette méthode n’est pas prise en charge </p></body></html>"
        http_405error = http_head.encode("ascii") + http_data.encode("utf8")
        http_response = http_405error
        
    if method == "GET":
        #print(Path+data_ressource) #to print the path to the file
        if data_ressource == "/":
            data_ressource = "/index.html"
            
        if os.path.isfile(Path+data_ressource):
            extension = data_ressource[data_ressource.rfind('.')+1:]
            r = ("HTTP/1.1 200 OK\r\n").encode('ascii')
            reply = "Date: Tuesday, 28 Mar 2023 16:48:13 GMT\r\n"
            reply += "Expires: -1\r\n"
            reply += "Cache-Control: private, max-age=0\r\n"
            reply += "Content-Type:"+dct[extension]+"\r\n"
            reply += "charset=ISO-8859-1\r\n\r\n"
            f = open(Path+data_ressource,'rb')
            dataf= f.read()
            f.close()
            http_response = r+reply.encode("utf8")+dataf

        else :
            http_head = "HTTP/1.1 404 Not found\r\n\r\n"
            http_data = "<html><body><p>404 not found</p></body></html>\r\n"
            http_404error = http_head.encode("ascii") + http_data.encode("utf8")
            http_response = http_404error
    
    if data_ressource == "/exit" :
        break
    
    s.send(http_response)  
    print('sending data...\n') 
    s.close()

print('Socket closed.')    
sconn.close()

