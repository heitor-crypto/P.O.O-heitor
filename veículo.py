class Veiculo:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano
        
    def fazer_som(self):
        print("o veiculo buzina")
        
class Carro(Veiculo):
    def __init__(self, modelo, ano, portas):
        super().__init__(modelo, ano)
        self.portas = portas
    
    def __str__(self):
        return f"carro - modelo e ano: {self.modelo} {self.ano}\n"
    def abrir_portas(self):
        print(f"{self.modelo} abriu as portas")
        
class Moto(Veiculo):

    def __str__(self):
        return f" moto - modelo e ano: {self.modelo} {self.ano}\n"
        
    def empinar(self):
        print(f"{self.modelo} empinou!")
        
moto = Moto("yamaha", 2010)
moto.empinar()
print(moto)
carro = Carro("fusca azul", 2008, 2)
carro.abrir_portas()
print(carro)
