import unittest
from calculadora import Calculadora


class TestesCalculadora(unittest.TestCase):
    def teste_soma(self):
        calcula = Calculadora()
        resultadosoma = calcula.calcular(15, 15, "soma")
        self.assertEqual(resultadosoma, 30)

    def teste_subtracao(self):
        calcula = Calculadora()
        resultadosubtracao = calcula.calcular(5, 3, "subtracao")
        self.assertEqual(resultadosubtracao, 2)

    def teste_divisao(self):
        calcula = Calculadora()
        resultadodivisao = calcula.calcular(50, 2, "divisao")
        self.assertEqual(resultadodivisao, 25)

    def teste_erro_de_operador(self):
        calcula = Calculadora()
        resultadodivisao = calcula.calcular(50, 2, "divis")
        self.assertEqual(resultadodivisao, "Operador inválido!")

    def teste_erro_de_operador_vazio(self):
        calcula = Calculadora()
        resultado = calcula.calcular(50, 2, "")
        self.assertEqual(resultado, "Operador inválido!")


if __name__ == '__main__':
    unittest.main()
