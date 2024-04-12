import pandas as pd
import random


def criar_usuario(lista_usuarios, dfusuario):
    nome = input("Qual o seu nome?:")
    data = input("Qual a data de nascimento?:")
    cpf = input("Qual o seu CPF?:")
    df = dfusuario.append({'nome': nome, 'data_nasc': data, 'CPF': cpf}, ignore_index=True)
    lista_usuarios.append(df)

def criar_conta(contas, lista_usuarios, dfcontas):
    nome = input('Qual o seu nome:')
    if lista_usuarios != None:
        for usuario in lista_usuarios:
            if nome == usuario['nome'].iloc[0]:
                agencia =random.randint(0,10)
                num_conta = '0001' + str(random.randint(0, 9999)).zfill(4)  
                user = nome
                df = dfcontas.append({'agencia': agencia, 'numero da conta': num_conta, 'usuario': user}, ignore_index=True)
                contas.append(df)
            else:
                return print("Usuario não encontrado")
    else:
        return print("Lista vazia")
        
            

def deposito():
    global conta 
    depost = float(input('Deseja depositar que valor?:'))
    if depost <= 0:
        print('Valor nulo ou invalido')
        return conta
    conta += depost
    return conta

def extrato():
    global conta, quant_saque, quant_depo
    if quant_depo != 0 or quant_saque != 0:
        return print(f'R$ {conta}, Quantidade de saques: {quant_saque}, Quantidade de depositos: {quant_depo}')
    else:
        return print('Não foram realizadas movimentações')
    
def saque():
    global conta 
    saca = float(input('Deseja sacar que valor?:'))
    if saca <= 0 or saca > conta or saca > 500:
        print('Valor nulo ou invalido')
        return conta
    conta -= saca
    return conta

frase = '''\n1 para deposito
2 para saque
3 para extrato
4 para cadastrar usuario
5 para criar conta
Digite qualquer outra tecla para cancelar\n'''

digito = int(input(frase))

conta = 0
limitador = 0
quant_depo = 0
quant_saque = 0
lista_usuarios = []
contas = []
dfusuario = pd.DataFrame(columns=['nome', 'data_nasc', 'CPF'])
dfconta = pd.DataFrame(columns=['agencia', 'numero da conta', 'usuario'])
while digito >= 0:
    match digito:
        case 1:
            quant_depo += 1
            deposito()
            digito = int(input(frase))
        case 2:
            limitador += 1
            if limitador <= 3:
                quant_saque += 1
                saque()
            digito = int(input(frase))
        case 3:
            extrato()
            digito = int(input(frase))
        case 4:
            criar_usuario(lista_usuarios, dfusuario)
            digito = int(input(frase))
        
            print(lista_usuarios)
        case 5:
            criar_conta(contas, lista_usuarios, dfconta)
            print(contas)
            digito = int(input(frase))
            
        case _:
            break
        
        