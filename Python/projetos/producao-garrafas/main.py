try:
    with open("valor_anterior.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    historico = []
    for linha in linhas:
        numero = int(linha.strip())
        historico.append(numero)

    valor_anterior = historico[-1]

except:
    historico = []
    valor_anterior = 0

try:
    with open("bebida_anterior.txt", "r") as arquivo:
        linhas = arquivo.read()

    bebida_anterior = linhas.strip()

except:
    bebida_anterior = ""

maquina = int(input("Qual máquina: "))
bebida = input("Qual bebida está rodando: ")

metas = {
    5: {
        "coca cola": 26000,
        "tetris": 26000,
        "fanta laranja": 26000,
        "fanta guarana": 26000,
        "fanta uva": 26000
    },
    7: {
        "coca cola 1l": 28800,
        "coca cola 1,5l": 25000,
        "coca cola 2,25l": 22000,
        "coca cola 2,5l": 18000,
        "sprite lemon": 25000,
        "fanta laranja": 22000,
        "citrus": 25000
    },
    8: {
        "coca cola": 27200
    },
    9: {
        "powerade": 21500,
        "del valle": 24500,
        "del valle limao": 24500,
        "power acai": 24500,
        "cha matte": 24500
    },
    13: {
        "coca cola 2l": 24000,
        "coca cola 2,5l": 22800,
        "coca cola 3l": 19500
    }
}

meta = metas[maquina][bebida.lower()]

valor_atual = int(input("Digite o valor atual de garrafas da máquina: "))

if valor_atual < valor_anterior:
    producao_hora = valor_atual
else:
    producao_hora = valor_atual - valor_anterior

with open("bebida_anterior.txt", "w") as arquivo:
    arquivo.write(bebida)

if len(historico) >= 12 or valor_atual < valor_anterior or bebida.lower() != bebida_anterior.lower():
    historico = []

historico.append(valor_atual)

with open("valor_anterior.txt", "w") as arquivo:
    for numero in historico:
        arquivo.write(str(numero) + "\n")

meta_por_minuto = meta/60

minutos_parados = (meta - producao_hora) / meta_por_minuto

minutos_parados = round(minutos_parados)

print(f"Produção da hora: {producao_hora}")
print(f"Minutos parados: {minutos_parados} minutos")