from database.database import conectar
from datetime import datetime

def cadastrar_produto():

    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade do produto: "))
    preco = float(input("Preço do produto: ").replace(",", ".")) # replace converte vírgula em ponto para aceitar ambos os formatos de decimal

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO produtos (nome, quantidade, preco)
        VALUES (?, ?, ?)
    """, (nome, quantidade, preco))
    
    conexao.commit()
    print("Produto cadastrado com sucesso!")

    cursor.close()
    conexao.close()

def listar_produtos():

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    if not produtos:
        print("Não existe produto cadastrado!")
    else:
        print("\n=== LISTA DE PRODUTOS ===")

        for produto in produtos:
            print(f"""
ID: {produto[0]}
Nome: {produto[1]}
Quantidade: {produto[2]}
Preço: {produto[3]}
------------------------
""")
    cursor.close()
    conexao.close()

def buscar_por_nome_produto():

    nome = input("Digite o nome do produto: ")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos WHERE nome = ?", (nome,))
    produtos = cursor.fetchall()

    if not produtos:
        print("Não existe produto nenhum cadastrado para buscar por nome!")
    else:
        print("\n=== PRODUTOS COM ESTE NOME ===")
        
        for produto in produtos:
            print(f"""
ID: {produto[0]}
Nome: {produto[1]}
Quantidade: {produto[2]}
Preço: {produto[3]}
------------------------
""")

    cursor.close()
    conexao.close()

def buscar_por_id_produtos():

    id = int(input("Digite o id do produto: "))
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos WHERE id = ?", (id,))
    produtos = cursor.fetchone() # fetchone retorna apenas um registro — ideal para busca por id único
    
    if not produtos:
        print("Não existe nenhum produto cadastrado para buscar por id!")
    else:
        print("\n=== PRODUTO COM ESSE ID ===")
        print(f"""
ID: {produtos[0]}
Nome: {produtos[1]}
Quantidade: {produtos[2]}
Preço: {produtos[3]}
------------------------
""")

    cursor.close()
    conexao.close()

def atualizar_produto():

    id = int(input("Digite o id do produto: "))
    
    print("O que deseja atualizar?")
    print("1 - Nome")
    print("2 - Quantidade")
    print("3 - Preço")

    opcao = int(input("Escolha: "))
    
    if opcao == 1:
        novo_valor = input("Novo nome: ")
        campo = "nome"
    elif opcao == 2:
        novo_valor = input("Nova quantia: ")
        campo ="quantidade"
    elif opcao == 3:
        novo_valor = input("Novo preço: ")
        campo = "preco"

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(f"UPDATE produtos SET {campo} = ? WHERE id = ?", (novo_valor, id)) # monta o SQL dinamicamente com o campo escolhido pelo usuário
    conexao.commit()

    print("Produto atualizado com sucesso!")

    cursor.close()
    conexao.close()

def deletar_produto():

    id = int(input("Digite o id do produto que deseja deletar: "))
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))
    conexao.commit()
    
    print("Produto deletado com sucesso!")

    cursor.close()
    conexao.close()