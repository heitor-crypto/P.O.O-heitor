
class Cachorro:
    def __init__(self, nome, idade, raca, comida):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.energia = 100
        self.comida = max(0, comida)
        self.acordado = False
        self.feliz = False

    def acordar(self):
        if self.acordado:
            print(f"{self.nome} já está acordado!")
        else:
            self.acordado = True
            print(f"{self.nome} acordou!")

    def dormir(self):
        if not self.acordado:
            print(f"{self.nome} já está dormindo!")
        else:
            self.acordado = False
            self.energia = 100
            print(f"{self.nome} está dormindo!")

    def brincar(self):
        if not self.acordado:
            print(f"{self.nome} está dormindo e não pode brincar!")
        elif self.energia < 20:
            print(f"{self.nome} não tem energia para brincar!")
        else:
            self.feliz = True
            self.energia -= 20
            print(f"{self.nome} está brincando e está feliz!")
            print(f"Energia restante: {self.energia}")

    def ignorar(self):
        self.feliz = False
        print(f"{self.nome} está triste!")

    def comer(self):
        if not self.acordado:
            print(f"{self.nome} está dormindo e não pode comer!")
        elif self.comida <= 0:
            print(f"{self.nome} está sem comida!")
        else:
            self.comida -= 1
            print(f"{self.nome} está comendo!")
            print(f"Comida restante: {self.comida}")

    def latir(self):
        if self.acordado:
            print(f"{self.nome} está latindo! Au au!")
        else:
            print(f"{self.nome} está dormindo e não pode latir!")

    def exibir_status(self):
        print("\n--- STATUS DO CACHORRO ---")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Raça: {self.raca}")
        print(f"Comida: {self.comida} unidades")
        print(f"Acordado: {self.acordado}")
        print(f"Feliz: {self.feliz}")
        print(f"Energia: {self.energia} unidades")
        print("--------------------------\n")


if __name__ == "__main__":
    cachorro1 = Cachorro("Max", 3, "Vira-lata", 8)

    cachorro1.exibir_status()

    cachorro1.brincar()
    cachorro1.acordar()

    cachorro1.brincar()
    cachorro1.brincar()
    cachorro1.brincar()
    cachorro1.brincar()
    cachorro1.brincar()
    cachorro1.brincar()

    cachorro1.exibir_status()

    cachorro1.dormir()
    cachorro1.acordar()
    cachorro1.brincar()

    cachorro1.comer()
    cachorro1.latir()
    cachorro1.ignorar()

    cachorro1.exibir_status()
