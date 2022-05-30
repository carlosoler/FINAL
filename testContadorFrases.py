import unittest
from ContadorFrases import *


class MyTestCase(unittest.TestCase):
    def test_ContarTotal(self):
        peticion = 'TOTAL'
        fichero = 'ficheroPrueba'
        cont = ContadorFrases()
        resultado = cont.calculador(peticion, fichero)
        esperado = "3 FRASES 1 LINEAS"
        self.assertEqual(esperado, resultado)



if __name__ == '__main__':
    unittest.main()
