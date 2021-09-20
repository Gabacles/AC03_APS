from operacoes import Divisao, Soma, Subtracao, Multiplicacao


class OperacaoFabrica():
    def criar(self, operador):
        if operador == "divisao":
            return Divisao()
        elif operador == "soma":
            return Soma()
        elif operador == "subtracao":
            return Subtracao()
        elif operador == "multiplicacao":
            return Multiplicacao()
