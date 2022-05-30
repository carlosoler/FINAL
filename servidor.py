import datetime, locale, socket
from ContadorFrases\
    import *
import errno
import os.path

fichero = 'DATOS'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(('0.0.0.0', 16023))
s.listen(1)

while True:
    ns, dir_cli = s.accept()
    try:
        peticion = ns.recv(100).decode('utf-8').strip()
        cont = ContadorFrases()
        resultado = cont.calculador(peticion, fichero)

        ns.send(resultado.encode('utf-8'))
        ns.close()
    except IOError as e:
        if e.errno == errno.EPIPE:
            print("ERROR")