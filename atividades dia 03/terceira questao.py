class Carro:
    def __init__(self, marca, modelo, ano, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade
        
    def acelerar(self, incremento):
        self.velocidade += incremento
        return f"O carro da marca {self.marca} {self.modelo} acelerou para {self.velocidade} km/h."
    
carro = Carro("Honda", "Civic", 2022, 176)

print(carro.acelerar(1))
print(carro.acelerar(2))
