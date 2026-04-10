# Jogo da advinhação
import random

numero_secreto = random.randint(1,100)
tentativas = 0
chute = 0
dificuldade = 0

dificuldade = int(input("Escolha a dificuldade: 1 = Fácil/ 2 = Difícil: "))

if dificuldade == 1:
    tentivas_max = 10
    # dicas normais

elif dificuldade == 2:
    tentivas_max = 5
    # dicas enigmaticas
    


while chute != numero_secreto and tentativas < tentivas_max:
    chute = int(input("Adivinhe o número de 1 a 100: "))
    tentativas += 1

    if dificuldade == 1:
        if chute < numero_secreto:
            print("O número é maior!")
        elif chute > numero_secreto:
            print("O número é menor!")
        else:
            print("Você acertou, Parabéns!!! :)")

    if dificuldade == 2:
        if abs(chute - numero_secreto) == 0:
            print("Você acertou na maior dificuldade, Parabéns você é algum tipo de gênio?? :)")
        elif abs(chute - numero_secreto) <= 5:
            print("Você está ouvindo os sussurros, está próximo...")
        elif chute < numero_secreto:
            print("As estrelas estão acima e longe de você, continue subindo.")
        elif chute > numero_secreto:
            print("Você foi longe demais nas estrelas, volte imediatamente para não se perder no universo.")

if tentivas_max == tentativas and chute != numero_secreto:
    if dificuldade == 1:
        print("Foi muito perto mas acabou suas tentativas...No mais fácil? ta de brincadeira em...")
    elif dificuldade == 2:
        print("Acabou suas tentativas mas relaxa, essa é a dificuldade mais alta, na próxima você consegue! :)")
