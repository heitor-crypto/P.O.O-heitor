
class Carro:
    def __init__(self, modelo: str, ano: int, cor: str):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.combustivel = 100
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if self.ligado:
            print("O carro já está ligado.")
        elif self.combustivel > 0:
            self.ligado = True
            print("Carro ligado.")
        else:
            print("Sem combustível para ligar o carro.")

    def desligar(self):
        if not self.ligado:
            print("O carro já está desligado.")
        elif self.velocidade == 0:
            self.ligado = False
            print("Carro desligado.")
        else:
            print("O carro precisa estar parado para desligar.")

    def acelerar(self):
        if not self.ligado:
            print("O carro está desligado.")
        elif self.combustivel <= 0:
            print("O carro está sem combustível.")
        else:
            self.velocidade += 10
            self.combustivel = max(0, self.combustivel - 5)
            print(f"Acelerando... Velocidade: {self.velocidade} km/h")

    def frear(self):
        if self.velocidade > 0:
            self.velocidade = max(0, self.velocidade - 10)
            print(f"Freando... Velocidade: {self.velocidade} km/h")
        else:
            print("O carro já está parado.")

    def abastecer(self, quantidade: int):
        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
        else:
            self.combustivel = min(
                100, self.combustivel + quantidade
            )
            print(f"Combustível: {self.combustivel}%")

    def buzinar(self):
        print("BEEEEEP!")

    def status(self):
        print("\n--- STATUS DO CARRO ---")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Cor: {self.cor}")
        print(f"Velocidade: {self.velocidade} km/h")
        print(f"Combustível: {self.combustivel}%")
        print(f"Ligado: {self.ligado}")
        print("-----------------------\n")


if __name__ == "__main__":
    meu_carro = Carro("Fusca", 1975, "Azul")

    meu_carro.status()
    meu_carro.ligar()

    meu_carro.acelerar()
    meu_carro.acelerar()
    meu_carro.acelerar()

    meu_carro.frear()
    meu_carro.abastecer(20)
    meu_carro.buzinar()
    meu_carro.status()

    meu_carro.desligar()

    meu_carro.frear()
    meu_carro.frear()

    meu_carro.desligar()
    meu_carro.status()
