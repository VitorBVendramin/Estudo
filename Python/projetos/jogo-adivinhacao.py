# Jogo da advinhação


# Regra do jogo: Acertar o número secreto, com dicas ou sem dicas, escolha sua própria dificuldade

Numero_secreto = 30
tentativa = 0

while tentativa != Numero_secreto:
    tentativa = int(input("Adivinhe o número de 1 a 100: "))

    if  tentativa < Numero_secreto:
        print("O número secreto é maior!")
    elif tentativa > Numero_secreto:
        print("O número secreto é menor!")
    else:
        print("Você acertou, Parabéns!")
