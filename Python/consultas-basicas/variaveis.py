# nome = "Vitor"       #variavel nome do tipo texto sempre entre aspas ("" ou '')
# idade = 22           #variavel idade do tipo inteiro (sem decimais)
# estudando_programacao = True  #variavel booleana, valor lógico (true/false)


# print(f"Opa, meu nome é {nome} e tenho {idade}.")

nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
programacao = input("voce gosta de programação? (sim/não): ")

gosta_programacao = programacao.lower() in ["sim", "s"]

print(f"Olá, meu nome é {nome}, tenho {idade} e é {'verdade' if gosta_programacao else 'falso'} que gosto de programação.")