#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket


hostName = string(input("Введите имя хоста: "))
portNumber = int(input("Введите номер порта: "))
sock = socket.socket()
if(hostName != ''):
    if(portNumber > 1024 and portNumber < 65536):
        sock.connect((hostname, portNumber))
    else: sock.connect((hostname, 9090))
elif(portNumber > 1024 and portNumber < 65536):
    sock.connect(('localhost', portNumber))
else: sock.connect(('localhost', 9090))

while True:
    word = input()
    if word =="":
        word = "exit"
    sock.send(word.encode())
    data = sock.recv(1024).decode()
    if "EXIT" in data:
        sock.close()
        break
    print(data)

