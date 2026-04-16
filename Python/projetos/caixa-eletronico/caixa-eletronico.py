from datetime import datetime

def sacar(saldo, extrato):
    sacar = float(input("Digite o valor do saque: "))
    horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    if sacar > saldo:
        print("Saldo insuficiente, operação não realizada")
    else:
        saldo -= sacar
        extrato.append(f"Saque de R${sacar:.2f} - {horario}")

    return saldo

def depositar(saldo, extrato):
    depositar = float(input("Digite o valor do depósito: "))
    horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    if depositar <= 0:
        print("Nenhum depósito foi feito, pois o número é menor que zero!")
    else:
        saldo += depositar
        extrato.append(f"Depósito de:R${depositar:.2f} - {horario}")
    
    return saldo


def consultar_saldo(saldo):
    print(f"Seu saldo atual é de:R${saldo:.2f}")

def ver_extrato(extrato):
    if not extrato:
        print("Nenhuma operação foi realizada ainda!")
    else:
        for operacao in extrato:
            print(operacao)


def menu():
    saldo = 0
    extrato = []
    while True:
        print("=== CAIXA ELETRÔNICO ===")
        print("1 - Sacar")
        print("2 - Depositar")
        print("3 - Consultar Saldo")
        print("4 - Ver Extrato")
        print("5 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            saldo = sacar(saldo, extrato)

        elif opcao == 2:
            saldo = depositar(saldo, extrato)
    
        elif opcao == 3:
            consultar_saldo(saldo)
    
        elif opcao == 4:
            ver_extrato(extrato)
        
        elif opcao == 5:
            break

        else:
            print("Número digitado é inválido, escolha entre 1 a 5!")

menu()

print("Operação finalizada!")