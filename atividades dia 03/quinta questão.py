class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def emitir_som(self):
        pass
    
    def informacoes_gerais(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"

class Cachorro(Animal):
    def emitir_som(self):
        return "AUUUUUU AUUUUUUUUUU!"
    
class Gato(Animal):
    def emitir_som(self):
        return "MIAUUUU!"

cachorro = Cachorro("Asta", 0.5)
print(cachorro.informacoes_gerais())
print("Som:", cachorro.emitir_som())

gato = Gato("Jhin", 0.4)
print(gato.informacoes_gerais())
print("Som:", gato.emitir_som())
