import unittest
from ContadorFrases import *


class MyTestCase(unittest.TestCase):
    def test_mostrarTotal(self):
        peticion = 'TOTAL'
        fichero = 'ficheroPrueba'
        cont = ContadorFrases()
        resultado = cont.calculador(peticion, fichero)
        esperado = "1 FRASES 1 LINEAS"
        self.assertEqual(esperado, resultado)

    def test_mostrarTotalOtroArchivo(self):
        peticion = 'TOTAL'
        fichero = 'DATOS'
        cont = ContadorFrases()
        resultado = cont.calculador(peticion, fichero)
        esperado = "5 FRASES 11 LINEAS"
        self.assertEqual(esperado, resultado)

    def test_mostrarTotalOtroArchivoII(self):
        peticion = 'TOTAL'
        fichero = 'ejemplo_passwd'
        cont = ContadorFrases()
        resultado = cont.calculador(peticion, fichero)
        esperado = "34 FRASES 35 LINEAS"
        self.assertEqual(esperado, resultado)

    def test_fraseAleatoria(self):
        peticion = 'FRASE'
        fichero = 'ficheroPrueba'
        cont = ContadorFrases()
        resultado = cont.calculador(peticion, fichero)
        esperado = "hola que tal"
        self.assertEqual(esperado, resultado)

    def test_fraseAleatoriaOtroArchivo(self):
        peticion = 'FRASE'
        fichero = 'hola'
        cont = ContadorFrases()
        resultado = cont.calculador(peticion, fichero)
        esperado = ""
        self.assertEqual(esperado, resultado)

    def test_ComprobarQueLaFraseEstaEnElFichero(self):
        peticion = 'FRASE'
        fichero = 'DATOS'
        cont = ContadorFrases()
        resultado = cont.calculador(peticion, fichero)
        fichero_abierto = open(fichero, "r")
        f = fichero_abierto.read()
        self.assertTrue(resultado in f)

    def test_ComprobarQueLaFraseNoEstaEnElFichero(self):
        peticion = 'FRASE'
        fichero = 'DATOS'
        cont = ContadorFrases()
        resultado = "subnormal"
        fichero_abierto = open(fichero, "r")
        f = fichero_abierto.read()
        self.assertFalse(resultado in f)

    def test_devolverError(self):
        peticion = 'hola'
        fichero = 'DATOS'
        cont = ContadorFrases()
        resultado = cont.calculador(peticion, fichero)
        esperado = "ERROR"
        self.assertEqual(esperado, resultado)

    def test_pasarFicheroQueNoExiste(self):
        peticion = 'FRASE'
        fichero = 'uuu'
        cont = ContadorFrases()
        resultado = cont.calculador(peticion, fichero)
        esperado = "ERROR"
        self.assertEqual(esperado, resultado)

    def test_probarFuncionalidadCompleta(self):
        peticion = 'TOTAL'
        fichero = 'Makefile'
        cont = ContadorFrases()
        resultado = cont.calculador(peticion, fichero)
        esperado = "10 FRASES 15 LINEAS"
        self.assertEqual(esperado, resultado)

    def test_probarFicheroServices(self):
        peticion = 'TOTAL'
        fichero = 'ejemplo_services'
        cont = ContadorFrases()
        resultado = cont.calculador(peticion, fichero)
        esperado = "11159 FRASES 11177 LINEAS"
        self.assertEqual(esperado, resultado)

    def test_probarenviarTOTALenMinusculas(self):
        peticion = 'total'
        fichero = 'ejemplo_services'
        cont = ContadorFrases()
        resultado = cont.calculador(peticion, fichero)
        esperado = "ERROR"
        self.assertEqual(esperado, resultado)

if __name__ == '__main__':
    unittest.main()
