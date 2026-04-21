# Estrutura que permitem o programa tomar decisões com base em determinadas condições.

# Exemplo: 

# Você está navegando na Steam procurando um jogo e tem pouco dinheiro na carteira da steam.
# GTA 5 custa 15 reais, Dying light custa 11 reais e o Minecraft custa 8 reais.

# Se você tiver 15 reais ou mais na carteira steam, pode comprar GTA 5. >= 15
# Se você tiver 11 reais ou mais, pode comprar o Dying light. >= 11
# Se não compra o Minecraft. <=8

# if - "se"
# else - "se não"
# elif - "se + se não"

# if ComprarGTA5:
    # Executa quando a primeira condição for verdadeira.
# elif ComprarDyingLight:
    # Executa quando a primeira condição for falsa e a segunda verdadeira.
# else:
    # Executa quando nenhuma condição anterior for verdadeira.