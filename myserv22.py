#!/usr/bin/env python

import logging
import socket


logging.basicConfig(filename="logfile.log", level=logging.INFO)
portNumber = int(input("Введите номер порта: "))
sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
if(portNumber > 1024 and portNumber < 65536):
        sock.bind(('', portNumber))
    else: sock.bind(('', 9090))

sock.listen(1)
conn, addr = sock.accept()
 
print('connected:', addr)

while True: 
    while True:
        data = conn.recv(1024).decode()
        logging.info(string(data))
        if not data:
            break
        conn.send(data.upper().encode())
        if "exit".lower() in data:
            break
    if ("exit".lower() in data) or not data:
        break
conn.close()
