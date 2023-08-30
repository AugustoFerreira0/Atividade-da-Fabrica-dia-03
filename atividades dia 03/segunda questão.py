class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def deposito(self, saldo):
        if saldo > 0:
            self.saldo += saldo
            return f"O deposito de R${saldo:2f} Foi realizado com sucesso!"
    
    def sacar(self, saldo):
        if saldo > 0 and saldo <= self.saldo:
            self.saldo -= saldo
            return f"Saque de R${saldo:.2f} realizado."
        else:
            return "Saldo insuficiente ou saldo de saque inválido."
        
conta = ContaBancaria("Augusto", 10000)

print("O titular da conta é: ", conta.titular)
print(conta.deposito(3000))
print(conta.sacar(50))
print(conta.sacar(1000))