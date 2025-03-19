class Carro:
    def __init__(self, modelo: str, ano: int, cor: str):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.combustivel = 100  
        self.ligado = False
        self.velocidade = 0
    
    def ligar(self):
        if self.combustivel > 0:
            self.ligado = True
            print("Carro ligado.")
        else:
            print("Sem combustível para ligar o carro.")
    
    def desligar(self):
        if self.velocidade == 0:
            self.ligado = False
            print("Carro desligado.")
        else:
            print("O carro precisa estar parado para desligar.")
    
    def acelerar(self):
        if self.ligado and self.combustivel > 0:
            self.velocidade += 10
            self.combustivel = max(0, self.combustivel - 5)
            print(f"Acelerando... Velocidade atual: {self.velocidade} km/h")
        else:
            print("Não é possível acelerar. O carro está desligado ou sem combustível.")
    
    def frear(self):
        if self.velocidade > 0:
            self.velocidade = max(0, self.velocidade - 10)
            print(f"Freando... Velocidade atual: {self.velocidade} km/h")
        else:
            print("O carro já está parado.")
    
    def abastecer(self, quantidade: int):
        self.combustivel = min(100, self.combustivel + quantidade)
        print(f"Carro abastecido. Nível de combustível: {self.combustivel}%")
    
    def buzinar(self):
        print("BEEEEEEEPPPP!")
    
    def status(self):
        estado = "Ligado" if self.ligado else "Desligado"
        print(f"Modelo: {self.modelo}, Ano: {self.ano}, Cor: {self.cor}, Velocidade: {self.velocidade} km/h, Combustível: {self.combustivel}%, Estado: {estado}")

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
meu_carro.frear()
meu_carro.desligar()
