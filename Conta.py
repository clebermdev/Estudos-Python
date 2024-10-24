class Conta:
    def __init__(self, titular, numero, saldo):
       self.saldo=0
       self.numero=numero
       self.titular=titular


    def get_saldo(self):
        return self.saldo

    def set_saldo(self, saldo):
        if (saldo<0):
            print("O Saldo não pode ser negativo")
        else:
            self._saldo=saldo

    def saque(self, valor):
        if (self.saldo>=valor):
            self.saldo-=valor
            print('Saque no valor de' , valor, 'realizado com sucesso')
        else:
            print('Saldo insuficiente')

    def depositar(self, valor):
        self.saldo+=valor
        print('Deposito no valor de' , valor, 'realizado com sucesso')

    def extrato(self, saldo):
        print(self.titular, ' seu saldo atual é: ', self.saldo)