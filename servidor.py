import datetime, locale, socket
import sys

from ContadorFrases\
    import *
import errno
import os.path

fichero = 'frases'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(('0.0.0.0', 16023))
s.listen(1)

while True:
    ns, dir_cli = s.accept()
    print(dir_cli, file=sys.stderr)
    try:
        peticion = ns.recv(100).decode('utf-8').strip()
        print(peticion, file=sys.stderr)
        cont = ContadorFrases()
        resultado = cont.calculador(peticion, fichero)

        ns.sendto(resultado.encode('utf-8'),dir_cli)
        ns.close()

    except IOError as e:
        if e.errno == errno.EPIPE:
            print("ERROR")