#Apresentação

from random import randint


print('=-'*15,'BEM VINDO AO BANCO JEYSONCARD.', '=-'*15)

print('=-'*15,'Preencha seus dados corretamente para prosseguir','=-'*15)

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



#começo
resp = ' '
while resp not in 'UN':
    resp = str.upper(input('VOCÊ JÁ É USÚARIO DO BANCO OU É NOVATO E DESEJA FAZER UM CADASTRO?[U/N]: '))


#Banco de Dados.
lista = [['JEYSON SARAIVA VIEIRA', '086409511', '55385554960', '307119', 3200],
 ['ISADORA SOUSA DE CARVALHO', '019331863', '49538001541', '182315', 1800],
 ['EDUARDO RIBEIRO MOURA', '071151587', '38117715120', '540820', 2400]]


novo_usuario = list()
#Informações do Cliente
nome = ' '
if resp == 'U':
    nome = str.upper(input('Digite seu nome completo: '))


    if nome == lista[0][0]:
        posiçao = 0

    elif nome == lista[1][0]:
        posiçao = 1

    elif nome == lista[2][0]:
        posiçao = 2
        
    if nome == lista[0][0] or lista[1][0] or lista[2][0]:
        cartao = cpf = senha = ' '
        while cartao != lista[posiçao][1]:
            cartao = str(input('Digite o número do seu cartão: '))
            if cartao != lista[posiçao][1]:
                print('NÚMERO DO CARTÃO NÃO CORRESPONDETE! TENTE NOVAMENTE.')
        while cpf != lista[posiçao][2]:
            cpf = str(input('Digite o número do seu cpf: '))
            if cpf != lista[posiçao][2]:
                print('NÚMERO DO CPF NÃO CORRESPONDENTE! TENTE NOVAMENTE.')
        while senha != lista[posiçao][3]:
            senha = str(input('Digite sua senha: '))
            if senha != lista[posiçao][3]:
                print('SENHA INCORRETA, TENTE NOVAMENTE.')

        #print(lista[posiçao])
        cliente = Cliente(Nome = lista[posiçao][0], Cartão = lista[posiçao][1], Cpf = lista[posiçao][2], Senha = lista[posiçao][3], Saldo = lista[posiçao][4])


    else:
        print('SEU NOME NÃO FOI ENCONTRADO NO BANCO DE DADOS, CORRIGA SEU NOME OU FAÇA UM CADASTRO COM SEU NOME NO BANCO.')

if resp == 'N':
    print('=-'*15, 'VAMOS FAZER UM CADASTRO PARA VOCÊ', '=-'*15)
    novo_usuario.append(str.upper(input('Digite seu nome completo: ')))
    novo_usuario.append(randint(111111111, 999999999))
    novo_usuario.append(int(input('Digite seu cpf: ')))
    novo_usuario.append(int(input('Crie uma senha de 6 digitos: ')))
    novo_usuario.append(float(input('Digite seu saldo inicial: ')))
    #print(novo_usuario)
    cliente = Cliente(Nome = novo_usuario[0], Cartão = novo_usuario[1], Cpf = novo_usuario[2], Senha = novo_usuario[3], Saldo = novo_usuario[4])



# Interação com a maquina
print('[1] DEPOSITAR '
      '[2] SACAR '
      '[3] DADOS '
      '[4] SALDO ')


while True:
    resp = fim = ' '
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
        print(cliente.saldo)

    fim = str.upper(input('Deseja continuar?[S/N]: '))
    if fim == 'N':
        print('=-'*15,'OBRIGADO, VOLTE SEMPRE!','=-'*15)
        break
    #Fim