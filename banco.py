#Apresentação
#from concurrent.futures.process import _SafeQueue
#from tkinter.filedialog import SaveFileDialog
#from typing_extensions import Self


print('=-'*15,'BEM VINDO AO BANCO JEYSONCARD.', '=-'*15)

print('=-'*15,'Preencha seus dados corretamente para prosseguir''=-'*15)
#Cliente
class Cliente():
    def __init__(self, Nome, Cartão, Cpf, Senha, Saldo):
        self.nome = Nome
        self.cartao = Cartão
        self.cpf = Cpf
        self.senha = Senha
        self.saldo = Saldo


#Opções
    def total():
        return Cliente.saldo

    
    def deposito(self):
        self.saldo = self.saldo + depo
        return self.saldo

    def saque(self):
        self.saldo = self.saldo - saque
        return self.saldo

    def dados(self):
        Dados = self.nome, self.cartao, self.cpf, self.senha, self.saldo
        return Dados

    def saida(self):
        self.saida = 'obrigado, Volte sempre'
        return self.saida
#Informações do Cliente
nome = str(input('Digite seu nome completo: '))
cartao = int(input('Digite o número do seu cartão: '))
cpf = int(input('Digite o número do seu cpf: '))
senha = int(input('Digite sua senha: '))
saldo = float(input('Digite seu saldo: '))



cliente = Cliente(Nome = nome, Cartão = cartao, Cpf = cpf, Senha = senha, Saldo = saldo)

#Interação com a maquina
print('[1] DEPOSITAR '
      '[2] SACAR '
      '[3] DADOS '
      '[4] SAIR'
)
resp = ' '
while resp not in '1234':
    resp = str(input('Qual dessas opções deseja escolher?: '))
if resp == '1':
    print(cliente.saldo)
    depo = float(input('Qual valor deseja depositar?: '))
    print(cliente.deposito())

elif resp == '2':
    print(cliente.saldo)
    saque = float(input('Qual valor deseja sacar?: '))
    print(cliente.saque())

elif resp == '3':
    print(cliente.dados())

elif resp == '4':
    print(cliente.saida())

#Fim