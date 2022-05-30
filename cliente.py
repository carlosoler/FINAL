
import errno
import os
import socket

addres_serv = ('0.0.0.0', 16023)

peticion = input("Que desea?: FRASE o TOTAL: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 0))

try:
    s.connect(addres_serv)
    s.send(peticion.encode('utf-8'))

    recibido = s.recv(1000).decode('utf-8').strip()
    print(recibido)
    s.close()
except IOError as e:
    if e.errno == errno.EPIPE:
        pass