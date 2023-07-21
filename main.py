
def menu():
    print("""

============== Banco ==============

Operações:
- D: depósito em conta
- S: saque de dinheiro
- E: extrato
- N: novo usuário
- C: nova conta
- Q: sair da aplicação
          
====>  """, end="")
    return input().upper()

def depositar(saldo, deposito, extrato, /):
    if deposito > 0:
        saldo += deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"
    else:
        print("\nO valor informado é inválido! Tente novamente!")

    return saldo, extrato


def sacar(*, saldo, saque, extrato, limite, saques_realizados, limite_saques):
    if saque > saldo:
        print("\nO valor do saque excede o saldo da conta.")
    
    elif saques_realizados >= limite_saques:
        print("A quantidade máximas de saques já foi atingida (MAX.: 3 saques).")
    
    elif saque > limite:
        print(f"O valor do saque ultrapassou o limite de saque: R${limite},00.")
    
    elif saque > 0:
        saldo -= saque
        extrato += f"Saque: R$ {saque:.2f}\n"
        saques_realizados += 1
    
    else:
        print("O valor informado é inválido! Tente novamente!")
    
    return saldo, extrato, saques_realizados

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def buscar_usuario(usuarios, cpf):
    user = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return user[0] if len(user) > 0 else None

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (apenas números):  ")
    usuario = buscar_usuario(usuarios, cpf)

    if usuario:
        print("Usuário já existe!")
        return

    nome = input("Informe o nome: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, numero - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco, "cpf": cpf})

    print("\nUsuário inserido com sucesso!")

def criar_conta(usuarios, numero_conta, agencia):
    cpf = input("Informe o CPF (apenas números):  ")
    usuario = buscar_usuario(usuarios, cpf)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"usuario": usuario, "agencia": agencia, "conta": numero_conta}
    
    print("\nUsuário não encontrado! Encerrando criação de nova conta...")

def main():
    LIMITE_SAQUES = 3
    LIMITE = 500
    AGENCIA = "0001"

    saldo = 0
    saques_realizados = 0
    extrato = ""
    usuarios = []
    contas = []

    while True:

        cmd = menu()

        match cmd:
            case 'D':
                deposito = float(input("Digite a quantidade a ser depositada: "))

                saldo, extrato = depositar(saldo, deposito, extrato)
            case 'S':
                saque = float(input("Informe o valor do saque: "))

                saldo, extrato, saques_realizados = sacar(
                    saldo=saldo,
                    saque=saque,
                    extrato=extrato,
                    limite=LIMITE,
                    saques_realizados=saques_realizados,
                    limite_saques=LIMITE_SAQUES
                )
            case 'E':
                exibir_extrato(saldo, extrato=extrato)
            case 'N':
                criar_usuario(usuarios)
            case 'C':
                numero_conta = len(contas) + 1

                conta = criar_conta(usuarios, numero_conta, AGENCIA)
                
                if conta:
                    contas.append(conta)
            case 'Q':
                print("\nEncerrando aplicação...")
                print(usuarios)
                print(contas)
                break
            case _:
                print("Operação Inválida! Tente outro comando!")
main()