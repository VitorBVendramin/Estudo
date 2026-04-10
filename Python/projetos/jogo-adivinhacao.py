# Jogo da advinhação

numero_secreto = 30
tentativas = 0
chute = 0
dificuldade = 0

dificuldade = int(input("Escolha a dificuldade: 1 = Fácil/ 2 = Difícil: "))

if dificuldade == 1:
    tentivas_max = 15
    # dicas normais

elif dificuldade == 2:
    tentivas_max = 10
    # dicas enigmaticas
    


while chute != numero_secreto and tentativas < tentivas_max:
    chute = int(input("Adivinhe o número de 1 a 100: "))
    tentativas += 1

    if  chute < numero_secreto:
        print("O número secreto é maior!")
    elif chute > numero_secreto:
        print("O número secreto é menor!")
    else:
        print("Você acertou, Parabéns!")

if chute != numero_secreto:
    print("Você perdeu! O número secreto era", numero_secreto)
