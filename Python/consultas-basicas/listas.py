# Listas
# Definido entre [] e pode armazenar diferentes dados

# treino = ["academia", "natação", "volei"]
# numeros = [1, 2, 3, 4, 5]
# junto = ["academia", 2, "volei", 5]

# Acessando elementos da lista

# print(treino[0]) # "academia"
# print(treino[1]) # "natação"
# print(treino[2]) # "volei"
# print(treino[-1]) # "volei"

# Mudando valor na lista

# treino[1] = "tenis"
# treino[2] = "futebol"
# print(treino)

# append(): adiciona um item no final
# insert(): adiciona um item em uma posição especifica

# numeros = [17, 19, 20]

# numeros.append(21) # adiciona 21 no final da lista (17, 19, 20, 21)

# numeros.insert(1, 18) # posição, valor (posição 0 = num 17, posição 1 = num 19, posição 2 = num 20...)
# print(numeros) # 17, 18, 19, 20, 21 (inseriu o 18 na posição 1)

# Removendo elementos da lista

# remove(): remove um item pelo valor
# pop(): remove um item pelo índice (ou o ultimo item se nenhum índice for passado)

# jogos = ["GTA 6", "Valorant", "F1 24", "State of decay 2"]
# jogos.remove("F1 24")
# print(jogos) # GTA 6, Valorant, State of decay 2

# jogos.pop(1)
# print(jogos) # Valorant removido

# jogos.pop()
# print(jogos) # State of decay 2 removido (ultimo índice)

# Tuplas são listas mas imutáveis, criadas com ()
# valores = ("50", "30", "20")
# numeros = (2, 5, 3)

# Acessar elemento
# print(valores[1]) # 30
# print(numeros[2]) # 3

# valores [0] = "10" # Gerará erro pois as tuplas são imutáveis!

# convertendo entre listas e tuplas
# modificiar entre tupla e lista para modificar elementos

# tupla = (1, 2, 3)
# lista = list(tupla) # converte para lista
# lista.append(4)
# tupla = tuple(lista) # converte de volta para tupla
# print(tupla) # (1, 2, 3, 4)

# Usar tupla quando queremos que os valores não sejam alterados
# Para guardar dados fixos: coordenadas, meses do ano, dia da semana etc

dia = ("segunda", "terça", "quarta", "quinta")
print(dia[3]) # "quinta"
