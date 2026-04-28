from database.database import conectar

def cadastrar_produto():

    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade do produto: "))
    preco = float(input("Preço do produto: ").replace(",", "."))

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO produtos (nome, quantidade, preco)
        VALUES (?, ?, ?)
    """, (nome, quantidade, preco))
    
    conexao.commit()
    print("Produto cadastrado com sucesso!")

def listar_produtos():

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    for produto in produtos:
        print(produto)

def buscar_por_nome_produto():

    nome = input("Digite o nome do produto: ")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos WHERE nome = ?", (nome,))
    produtos = cursor.fetchall()
    
    for produto in produtos:
        print(produto)


def buscar_por_id_produtos():

    id = int(input("Digite o id do produto: "))
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos WHERE id = ?", (id,))
    produtos = cursor.fetchone()
    
    print(produtos)


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
    cursor.execute(f"UPDATE produtos SET {campo} = ? WHERE id = ?", (novo_valor, id))
    conexao.commit()

    print("Produto atualizado com sucesso!")

def deletar_produto():

    id = int(input("Digite o id do produto que deseja deletar: "))
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))
    conexao.commit()
    
    print("Produto deletado com sucesso!")