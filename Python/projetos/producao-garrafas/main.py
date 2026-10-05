# nome das variaveis que irei usar

# valor_anterior / número fixo por enquanto (exemplo: 463000)
# valor_atual / vem do input(), convertido pra int
# meta / número fixo por enquanto (exemplo: 24000) — é a "norma cadência" da máquina
# producao_hora / você calcula, não define valor direto (é o resultado de uma conta)
# meta_por_minuto / também calculado
# minutos_parados / também calculado

meta = 24500

valor_anterior = 205000

valor_atual = int(input("Digite o valor atual de garrafas da máquina: "))

producao_hora = valor_atual - valor_anterior

meta_por_minuto = meta/60

minutos_parados = (meta - producao_hora) / meta_por_minuto

minutos_parados = round(minutos_parados)

print(f"Produção da hora: {producao_hora}")
print(f"Minutos parados: {minutos_parados} minutos parados")