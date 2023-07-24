menu = """

[d] Depositar 
[s] Sacar 
[e] Extrato
[q] Sair
[nv] Novo usuario
[cc] Criar Conta

=>"""

numero_conta = 0
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
AGENCIA = "0001"

def saque(*, saldo,valor,extrato,limite,numero_saques,limite_saques):
    
    if valor > saldo:
        print("Saldo insuficiente")
        
    elif valor > limite:
        print("Limite por operação excedido !! ")
        
    elif numero_saques > LIMITE_SAQUES:
        print("Limite de saques diarios excedido !! ")
        
    elif valor > 0:

        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1        
        
    else:
        print("Valor informado invalido")  

    return saldo,extrato     
    
def deposito(saldo,valor,extrato,/):
    
    if valor > 0:

        saldo += valor
        extrato += f"Deposito : R$ {valor:.2f}\n"        
            
    else:
        print("Valor informado é negativo, por favor informe um valor valido")

    return saldo,extrato

def exibirExtrato(saldo,/,*,extrato):
    print("Extrato")
    print("\n=======================EXTRATO=======================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R${saldo:.2f}")
    print("=====================================================")

def criar_usuario(usuarios):

    cpf = input("Informe o CPF(somente numeros): ")
    
    if filtrar_usuario(cpf,usuarios):
        print("Já existe usuario com esse CPF!")
        return
    
    nome = input("Informe o nome do usuario: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço(logradouro, N° - bairro - cidade/Sigla estado): ")

    usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "cpf":cpf, "endereco":endereco})

def filtrar_usuario(cpf,usuarios):
    usuario_filtrado = []
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario_filtrado = usuario["cpf"]
            return usuario_filtrado[0]
    return None

def criar_conta(usuarios,numero_conta,AGENCIA):
    numero_conta += 1
    cpf = input("Informe o CPF (Somente numeros): ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("Ususario criado com suscesso")
        return {"agencia":AGENCIA,"numero_conta":numero_conta,"usuarios":usuarios}
    
    print("Usuario não encontrado !")

while True:

    opcao = input(menu)

    if opcao == "d":

        valor = float(input("Informe o valor a ser depositado :"))
        saldo, extrato = deposito(saldo,valor,extrato)  
       

    elif opcao == "s":

        valor = float(input("Informe o valor a ser Sacado :"))
        saldo, extrato = saque(saldo=saldo,valor=valor,extrato=extrato,limite=limite,numero_saques=numero_saques,limite_saques=LIMITE_SAQUES)
    
    elif opcao == "e":

        exibirExtrato(saldo,extrato=extrato)

    elif opcao == "nv":

        criar_usuario(usuarios)
        print(usuarios)

    elif opcao == "cc":

        conta = criar_conta(usuarios,numero_conta,AGENCIA)

        if conta:
            contas.append(conta) 

    
    elif opcao == "q":
        break

    else:
        print("Operação inválida !")