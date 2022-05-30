import random


class ContadorFrases:

    def calculador(self, peticion, fichero):
        if peticion.upper() == 'TOTAL':
            fichero_abierto = open(fichero, "r")
            f = fichero_abierto.read()
            lineas = f.count("\n") +1
            #lineas = str(len(fichero_abierto.readlines()))

            Counter = 0
            CoList = f.split("\n")
            for i in CoList:
                if i:
                    Counter += 1
            return '%d FRASES %d LINEAS' % (Counter, lineas)

        elif peticion.upper() == 'FRASE':
            fichero_abierto = open(fichero, "r")
            f = fichero_abierto.read()
            CoList = f.split("\n")

            return random.choice(CoList)
