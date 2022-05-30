import unittest
from ContadorFrases import *


class MyTestCase(unittest.TestCase):
    def test_ContarTotal(self):
        peticion = 'TOTAL'
        fichero = 'ficheroPrueba'
        cont = ContadorFrases()
        resultado = cont.calculador(peticion, fichero)
        esperado = "1 FRASES 1 LINEAS"


if __name__ == '__main__':
    unittest.main()
