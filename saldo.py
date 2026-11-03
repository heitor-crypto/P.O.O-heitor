
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print("Depósito realizado com sucesso.")
        else:
            print("O depósito deve ser maior que zero.")

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            print("Valor inválido.")


conta = ContaBancaria("Heitor", 945)

print("Saldo inicial:", conta.get_saldo())

conta.depositar(100)

print("Saldo após depósito:", conta.get_saldo())
