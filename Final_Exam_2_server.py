# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 10:55:59 2023

@author: Lucie
"""

import socket
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 55000
BUFFER_SIZE = 1024 

sconn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("binding to "+ TCP_IP +":"+str(TCP_PORT)," ...")
sconn.bind((TCP_IP, TCP_PORT))

print("Waiting client ...")
sconn.listen(1)
s, addr = sconn.accept()
print('Client connected with address:', addr)


data = s.recv(BUFFER_SIZE) 
name = socket.gethostname()
print("\nClient ",name,":", data.decode('ascii'))

#On récupère la string et la commande
data_decoded = data.decode('ascii')
data_d = data_decoded.split('\r\n')
data_final_line = data_d[-1]
data_line = data_final_line.split('&')
data_string = data_line[0].split('=')
data_command = data_line[1].split('=')
string = data_string[1]
command = data_command[1]

if command == 'len':
    reponse = str(len(string))
    
if command == 'isdigit':
    reponse = str(string.isdigit())
    
if command == 'upper' :
    reponse = string.upper()
    
if command =='':
    reponse = 'No command, try again.'
    
http_head = "HTTP/1.1 200 OK\r\n"
r = "Date:" + time.asctime() +"GMT\r\n"
r += "Content-Type: text/plain;\r\n"
r += "content-length:"+str(len(reponse))+"\r\n"

http_reponse = http_head + r + reponse
data = http_reponse.encode('ascii')
s.send(data)  
print('sending data...\n') 
D = data.decode('ascii')

s.close()
sconn.close()