import locale
from decimal import Decimal


class CaixaEletronico:
    def __init__(self, saldo):
        # Inicializa o objeto CaixaEletronico com um saldo inicial
        self.saldo = Decimal(saldo)
        # Define a formatação de moeda para o padrão brasileiro
        locale.setlocale(locale.LC_ALL, "pt_br")

    def consultar_saldo(self):
        # Retorna uma string formatada com o saldo atual
        return f"Seu saldo atual é {locale.currency(self.saldo, grouping=True)}"

    def depositar(self, valor):
        # Remove espaços e substitui vírgula por ponto, se presentes
        valor = str(valor).strip().replace(",", ".")

        # Tenta converter o valor recebido em um número Decimal
        try:
            valor = Decimal(valor)
        except:
            return "Valor de depósito inválido."

        if valor > 0:
            # Realiza o depósito se o valor for positivo
            self.saldo += valor
            return f"Depósito de {locale.currency(valor, grouping=True)} realizado com sucesso."
        else:
            # Retorna mensagem se o valor não for positivo
            return "O valor deve ser maior que zero."

    def sacar(self, valor):
        # Remove espaços e substitui vírgula por ponto, se presentes
        valor = str(valor).strip().replace(",", ".")

        # Tenta converter o valor recebido em um número Decimal
        try:
            valor = Decimal(valor)
        except:
            return "Valor de saque inválido."

        if valor > self.saldo:
            # Retorna mensagem se o valor do saque for maior que o saldo
            return "Saldo insuficiente."

        if valor > 0:
            # Realiza o saque se o valor for positivo
            self.saldo -= valor
            return f"Saque de {locale.currency(valor, grouping=True)} realizado com sucesso."
        else:
            # Retorna mensagem se o valor não for positivo
            return "O valor deve ser maior que zero."
