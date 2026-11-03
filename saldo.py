
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = max(0, saldo)

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado.")
        else:
            print("O depósito deve ser maior que zero.")

    def sacar(self, valor):
        if valor <= 0:
            print("O saque deve ser maior que zero.")
        elif valor > self.__saldo:
            print("Saldo insuficiente.")
        else:
            self.__saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado.")

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            print("Valor inválido.")

    def exibir_status(self):
        print("\n--- DADOS DA CONTA ---")
        print(f"Titular: {self.titular}")
        print(f"Saldo: R$ {self.__saldo:.2f}")
        print("----------------------\n")


if __name__ == "__main__":
    conta = ContaBancaria("Heitor", 945)

    conta.exibir_status()

    conta.depositar(100)
    conta.exibir_status()

    conta.sacar(50)
    conta.exibir_status()

    conta.sacar(2000)
    conta.depositar(-10)

    print(f"Saldo final: R$ {conta.get_saldo():.2f}")
