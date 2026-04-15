saldo = 1000
extrato = []

def sacar(saldo):
    sacar = float(input("Digite o valor do saque: "))

    if sacar > saldo:
        print("Saldo insuficiente, operação não realizada")
    else:
        saldo -= sacar
        print(f"Saque efetuado! Novo saldo é de:R${saldo:.2f}")

    return saldo

def depositar(saldo):
    depositar = float(input("Digite o valor do depósito: "))

    if depositar <= 0:
        print("Nenhum depósito foi feito, pois o número é menor que zero!")
    else:
        saldo += depositar
        print(f"Depósito efetuado com succeso, seu novo saldo é de:R${saldo:.2f}")
    
    return saldo


def consultar_saldo(saldo):
    print(f"Seu saldo atual é de:R${saldo:.2f}")

def ver_extrato(extrato):
    


def menu():
    while True:
        print("=== CAIXA ELETRÔNICO ===")
        print("1 - Sacar")
        print("2 - Depositar")
        print("3 - Consultar Saldo")
        print("4 - Ver Extrato")
        print("5 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            saldo = sacar(saldo)

        elif opcao == 2:
            saldo = depositar(saldo)
    
        elif opcao == 3:
            consultar_saldo()
    
        elif opcao == 4:
            ver_extrato()
        
        elif opcao == 5:
            break

        else:
            print("Número digitado é inválido, escolha entre 1 a 5!")

print("Operação finalizada!")