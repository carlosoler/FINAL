import random


class ContadorFrases:

    def calculador(self, peticion, fichero):
        fichero_abierto = open(fichero, "r")
        f = fichero_abierto.read()
        ficheroSinSaltoLinea = f.split("\n")
        if peticion.upper() == 'TOTAL':
            lineas = f.count("\n") + 1
            contador = 0
            for frase in ficheroSinSaltoLinea:
                if frase:
                    contador += 1
            return '%d FRASES %d LINEAS' % (contador, lineas)

        elif peticion.upper() == 'FRASE':
            return random.choice(ficheroSinSaltoLinea)

        else:
            return "ERROR"
