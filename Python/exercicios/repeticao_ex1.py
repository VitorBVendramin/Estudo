senha_correta = "12345" # Valor da senha correta
senha = ""

for senha in range(5): # Limite de 5 tentativas
    senha = input("digite a senha: ") # Onde o usuário coloca a senha
    if senha == senha_correta: # Só libera o acesso se a senha for exatamento igual ao valor
        print("Acesso liberado")
        break

else:
    print("Limite excedido, tente novamente mais tarde!") # Caso a pessoa tente mais de 5x o código atinge o limite