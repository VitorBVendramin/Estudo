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

meta = 24500

bebida = input("Digite a bebida que esta rodando: ")

if bebida.lower() == "powerade":
    meta = 21500

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