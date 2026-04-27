# Jogo da advinhação
import random

numero_secreto = random.randint(1,100)
tentativas = 0
chute = 0
dificuldade = 0


dificuldade = int(input("Escolha a dificuldade: 1 = Fácil, 2 = Normal, 3 = Difícil: "))

# Define o número máximo de tentativas com base na dificuldade escolhida
if dificuldade == 1:
    tentivas_max = 10
    # dicas normais

elif dificuldade == 2:
    tentivas_max = 7


elif dificuldade == 3:
    tentivas_max = 5
    # dicas enigmaticas
    

# Loop principal: roda até acertar ou acabar as tentativas
while chute != numero_secreto and tentativas < tentivas_max:
    chute = int(input("Adivinhe o número de 1 a 100: "))
    tentativas += 1

# ===== DICAS PARA DIFICULDADE FÁCIL =====
    if dificuldade == 1:
        if chute < numero_secreto:
            print("O número é maior!")
        elif chute > numero_secreto:
            print("O número é menor!")
        else:
            print("Você acertou, Parabéns!!! :)")

# ===== DICAS PARA DIFICULDADE NORMAL =====
    if dificuldade == 2:
        if abs(chute - numero_secreto) == 0:  # Calcula a distância entre o chute e o número secreto para dar dicas de proximidade
            print("Você acertou em cheio, Parabéns, que tal tentar no difícil?")

        elif abs(chute - numero_secreto) <= 5:
            print("Você sente o calor? A resposta está bem perto.")

        elif abs(chute - numero_secreto) <= 15:
            if chute < numero_secreto:
                 dica = random.choice([ # Escolhe uma dica aleatória para variar as respostas
                        "O número secreto é maior.",
                        "O número secreto habita as alturas, você ainda rasteja."])
                 print(dica)
                 
            elif chute > numero_secreto:
                dica = random.choice([
                        "O número secreto é menor.",
                        "Você foi além do horizonte, recue seus passos."])
                print(dica)
                
        elif abs(chute - numero_secreto) <= 30:
            if chute < numero_secreto:
                 dica = random.choice([
                        "O número secreto é maior.",
                        "Os ventos sopram para o alto, seu número está abaixo do destino."])
                 print(dica)
                 
            elif chute > numero_secreto:
                dica = random.choice([
                        "O número secreto é menor.",
                        "O alvo ficou para trás, volte ao caminho."])
                print(dica)
            
        elif abs(chute - numero_secreto) <= 100:
            if chute < numero_secreto:
                 dica = random.choice([
                        "O número secreto é muito maior.",
                        "Você está MUITO distânte do destino, vá muito mais longe."])
                 print(dica)
                 
            elif chute > numero_secreto:
                dica = random.choice([
                        "O número secreto é muito menor.",
                        "Você foi além do que os olhos podem ver, volte muito."])
                print(dica)

# ===== DICAS PARA DIFICULDADE DIFÍCIL =====
    if dificuldade == 3:
        if abs(chute - numero_secreto) == 0:
            print("Você acertou na maior dificuldade, Parabéns você é algum tipo de gênio?? :)")

        elif abs(chute - numero_secreto) <= 5:
            print("Você está ouvindo os sussurros, está próximo...")

        elif abs(chute - numero_secreto) <= 20:
            if chute < numero_secreto:
                 dica = random.choice([
                        "Você desceu demais, o caminho está acima.",
                        "A névoa acima de você esconde o segredo."])
                 print(dica)
            elif chute > numero_secreto:
                dica = random.choice([
                        "Retroceda, o segredo ficou para trás.",
                        "O portal ficou para trás, volte."])
                print(dica)

        elif abs(chute - numero_secreto) <= 40:
            if chute < numero_secreto:
                 dica = random.choice([
                        "O universo se expande para cima, siga-o.",
                        "Sua jornada ainda não chegou ao destino."])
                 print(dica)
            elif chute > numero_secreto:
                dica = random.choice([
                        "Você ultrapassou o segredo sem perceber.",
                        "O tesouro ficou enterrado atrás de você."])
                print(dica)

        elif abs(chute - numero_secreto) <= 60:
            if chute < numero_secreto:
                 dica = random.choice([
                        "O número secreto habita as alturas, você ainda rasteja.",
                        "Há um longo caminho antes de alcançar o topo."])
                 print(dica)
            elif chute > numero_secreto:
                dica = random.choice([
                        "Você foi longe demais, as raízes estão muito atrás.",
                        "Recue muito, você se perdeu no caminho."])
                print(dica)

        else:
            dica = random.choice([
                "...",
                "O silêncio é sua única resposta."])
            print(dica)

if tentivas_max == tentativas and chute != numero_secreto: # Verifica se o jogador perdeu (acabaram as tentativas)
    if dificuldade == 1:
        print("Foi muito perto mas acabou suas tentativas...No mais fácil? ta de brincadeira em...")

    elif dificuldade == 2:
        print("Foi quase, talvez essa não seja a dificuldade ideial para você.")
    
    elif dificuldade == 3:
        print("Acabou suas tentativas mas relaxa, essa é a dificuldade mais alta, na próxima você consegue! :)")

print("O número secreto era", numero_secreto)
