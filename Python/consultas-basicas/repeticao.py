# Repetição (for e while).
# Repetir uma ação quantas vezes precisar sem ter que ficar digitando a mesma coisa várias vezes igualmente.



# FOR -> Sabendo a quantia de vezes que a função vai ser executada.

# Estrutura:

# for variável in sequência:
    # Código que vai ser repetido x vezes.


# Contando números com o FOR de 1 a 15.

#for numero in range(1, 16):
#    print(numero)

# O range (1, 16) gera os números de 1 a 15, o último número do range não é incluído.
# Sempre colocar um número acima do resultado final, pois o último não é contado. Ex: contar até 20, colocaria (1, 21) pois o 21 não incluí.


# while -> Quando não sabemos a quantia e precisa que alguma condição seja falsa.
# Tomar cuidado com loops infinitos!!! Caso a condição nunca altere pra false o código nunca para de rodar.

# Contagem regressiva

# contador = 10

# while contador > 0:
#     print(contador)
#     contador -= 1   # Diminui 1 do contador a cada rep
# print("Contagem finalizada!")

# Senha até acertar

# senha_correta = "54321"
# senha = ""

# while senha != senha_correta:
#     senha = input("digite a senha: ")
# print("Acesso Liberado!")


senha_correta = "12345"
senha = ""

for senha in range(5):
    senha = input("digite a senha: ")
    if senha == senha_correta:
        print("Acesso liberado")
        break

else:
    print("Limite excedido, tente novamente mais tarde!")
