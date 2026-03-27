senha_correta = "12345"
senha = ""

for senha in range(5):
    senha = input("digite a senha: ")
    if senha == senha_correta:
        print("Acesso liberado")
        break

else:
    print("Limite excedido, tente novamente mais tarde!")