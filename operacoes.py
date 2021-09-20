from abc import ABC, abstractmethod


class Operacao(ABC):
    @abstractmethod
    def executar(self, valor1, valor2):
        pass


class Divisao(Operacao):
    def executar(self, valor1, valor2):
        resultado_divisao = valor1 / valor2
        return resultado_divisao


class Soma(Operacao):
    def executar(self, valor1, valor2):
        resultado_soma = valor1 + valor2
        return resultado_soma


class Subtracao(Operacao):
    def executar(self, valor1, valor2):
        resultado_subtracao = valor1 - valor2
        return resultado_subtracao


class Multiplicacao(Operacao):
    def executar(self, valor1, valor2):
        resultado_multiplicacao = valor1 * valor2
        return resultado_multiplicacao
