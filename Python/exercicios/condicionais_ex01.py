# Verificando se pode comprar o passaporte ou não

#Dinheiro_passaporte = int(input("Coloque quanto tem de dinheiro atual: ")) # Usuário coloca a quantia de dinheiro que tem para a compra

#if Dinheiro_passaporte >= 2500:
#    print("Você comprou o passaporte!")
#else:
#    print("Você não possuí a quantia necessária para a compra!")




valor_carteira = int(input("Insira o saldo da carteira digital: ")) # Usuário insere o valor da carteira digital.

if valor_carteira >= 100:
    print("Você concluiu a compra com sucesso!") # Caso usuário tenha 100 reais ou mais, compra será realizada.
elif valor_carteira == 0:
    print("Você não tem nenhum saldo restante!") # Caso usuário não tenha nenhum saldo.
else:
    print(f"Você não tem dinheiro suficiente para esta compra, porém ainda tem {valor_carteira} de saldo sobrando para uso!") # Caso usuário tenha entre 99 a 1 real de saldo.