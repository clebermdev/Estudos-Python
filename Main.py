class Main:
    pass
print("testando o objeto")

from Cliente import Cliente
from Conta import Conta


c1 = Cliente ('João', '51 99012-1718')
conta=Conta(c1.get_nome(), 1222, 0)


conta.depositar(100)
conta.saque(15)
conta.extrato(c1)

