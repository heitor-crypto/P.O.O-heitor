
class Veiculo:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    def fazer_som(self):
        print("O veículo está fazendo um som.")


class Carro(Veiculo):
    def __init__(self, modelo, ano, portas):
        super().__init__(modelo, ano)
        self.portas = portas

    def fazer_som(self):
        print(f"{self.modelo} está buzinando!")

    def abrir_portas(self):
        print(f"As {self.portas} portas do {self.modelo} foram abertas.")

    def __str__(self):
        return (
            f"Carro: {self.modelo} | "
            f"Ano: {self.ano} | "
            f"Portas: {self.portas}"
        )


class Moto(Veiculo):
    def fazer_som(self):
        print(f"{self.modelo} está acelerando!")

    def empinar(self):
        print(f"{self.modelo} empinou!")

    def __str__(self):
        return f"Moto: {self.modelo} | Ano: {self.ano}"


if __name__ == "__main__":
    moto = Moto("Yamaha", 2010)

    moto.empinar()
    moto.fazer_som()
    print(moto)

    print()

    carro = Carro("Fusca Azul", 2008, 2)

    carro.abrir_portas()
    carro.fazer_som()
    print(carro)
