import unittest
from calculadora import *

class OperacaoTests(unittest.TestCase):
    def testar_adicao(self):
        adicao = Adicao()
        resultado = adicao.calcular(1,2)
        self.assertEqual(3, resultado)

    def testar_subtracao(self):
        subtracao = Subtracao()
        resultado = subtracao.calcular(1,2)
        self.assertEqual(-1, resultado)