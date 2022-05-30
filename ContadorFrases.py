import random


class ContadorFrases:

    def calculador(self, peticion, fichero):
        if peticion.upper() == 'TOTAL':
            fichero_abierto = open(fichero, "r")
            f = fichero_abierto.read()
            lineas = f.count("\n") +1
            contador = 0
            ficheroSinSaltoLinea = f.split("\n")
            for frase in ficheroSinSaltoLinea:
                if frase:
                    contador += 1
            return '%d FRASES %d LINEAS' % (contador, lineas)

        elif peticion.upper() == 'FRASE':
            fichero_abierto = open(fichero, "r")
            f = fichero_abierto.read()
            ficheroSinSaltoLinea = f.split("\n")
            return random.choice(ficheroSinSaltoLinea)
