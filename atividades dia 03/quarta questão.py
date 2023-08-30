import math

class FormaGeometrica:
    def calcular_area(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        return self.base * self.altura

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
        
    def calcular_area(self):
        return math.pi * self.raio ** 2

retangulo = Retangulo(12, 6)
print("Área do retângulo:", retangulo.calcular_area())

circulo = Circulo(10)
print("Área do círculo:", circulo.calcular_area())
