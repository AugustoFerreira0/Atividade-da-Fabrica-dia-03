class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        
    def saudacao(self):
        return f"Oi! Me chamo {self.nome}, tenho {self.idade} anos e sou {self.profissao}."

pessoa1 = Pessoa("Augusto Ferreira", 20, "Auxiliar de rede")

print(pessoa1.saudacao())


