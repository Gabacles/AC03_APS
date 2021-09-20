from operacaoFabrica import OperacaoFabrica


class Calculadora():
    def calcular(self, valor1, valor2, operador):
        tipoOperacao = OperacaoFabrica()
        operacao = tipoOperacao.criar(operador)
        try:
            resultado = operacao.executar(valor1, valor2)
            return resultado
        except AttributeError:
            return "Operador inválido!"
