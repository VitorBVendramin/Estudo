from database.database import conectar
from datetime import datetime

def registrar_venda():
    cliente_id = int(input("ID do cliente: "))
    produto_id = int(input("ID do produto: "))
    quantidade = int(input("Quantidade: "))


    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes WHERE id = ?", (cliente_id,))
    cliente = cursor.fetchone() # verifica se o cliente existe antes de prosseguir

    if cliente is None:
        print("Cliente não encontrado!")

        cursor.close()
        conexao.close()
        return

    cursor.execute("SELECT * FROM produtos WHERE id = ?", (produto_id,))
    produto = cursor.fetchone()
    if produto is None:
        print("Produto não encontrado!")

        cursor.close()
        conexao.close()
        return
    
    if produto[2] < quantidade: # verifica se o produto existe e tem estoque suficiente
        print("Estoque insuficiente!")

        cursor.close()
        conexao.close()
        return
    
    valor = produto[3] * quantidade # calcula o valor total: preço unitário × quantidade

    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    cursor.execute("""
    INSERT INTO vendas (cliente_id, produto_id, quantidade, valor, data)
    VALUES (?, ?, ?, ?, ?)
""", (cliente_id, produto_id, quantidade, valor, data))
    
    # diminui o estoque do produto após registrar a venda
    cursor.execute("""
    UPDATE produtos SET quantidade = quantidade - ? WHERE id = ?
""", (quantidade, produto_id))
    
    conexao.commit()
    print("Venda registrada com sucesso!")  

    cursor.close()
    conexao.close()

def listar_vendas():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM vendas")
    vendas = cursor.fetchall()

    if not vendas:
        print("Nenhuma venda encontrada!")
    else:
        print("\n=== LISTA DE VENDAS ===")
        for venda in vendas:
            print(f"""
ID da venda: {venda[0]}
ID do cliente: {venda[1]}
ID do produto: {venda[2]}
Quantidade: {venda[3]}
Valor: R${venda[4]:.2f}
Data: {venda[5]}
------------------------
""")

    cursor.close()
    conexao.close()

def vendas_por_produto():
    produto_id = int(input("ID do produto: "))

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos WHERE id = ?", (produto_id,))
    produto = cursor.fetchone()

    if produto is None:
        print("Produto não encontrado!")
    else:
        cursor.execute("SELECT * FROM vendas WHERE produto_id = ?", (produto_id,))
        vendas = cursor.fetchall()
    
        if not vendas:
            print("Nenhuma venda encontrada para este produto.")
        else:
            print(f"\n=== VENDAS DO PRODUTO: {produto[1]} ===")

            for venda in vendas:
                print(f"""
ID da venda: {venda[0]}
Cliente ID: {venda[1]}
Quantidade vendida: {venda[3]}
Valor total: R${venda[4]:.2f}
Data: {venda[5]}
------------------------
""")

    cursor.close()
    conexao.close()

def produtos_mais_vendido():
    conexao = conectar()
    cursor = conexao.cursor()

    # ORDER BY DESC ordena do maior para menor, LIMIT 3 retorna os 3 mais vendidos
    # SUM soma as quantidades vendidas, GROUP BY agrupa por produto
    cursor.execute("""
        SELECT p.nome, SUM(v.quantidade)
        FROM vendas v
        JOIN produtos p ON v.produto_id = p.id
        GROUP BY p.nome
        ORDER BY SUM(v.quantidade) DESC 
        LIMIT 3
    """)

    produtos = cursor.fetchall()

    if not produtos:
        print("Nenhuma venda registrada.")
    else:
        print("\n=== OS 3 PRODUTOS MAIS VENDIDOS ===")
    
    for produto in produtos:
        print(f"""
Produto: {produto[0]}
Quantidade vendida: {produto[1]}
------------------------
""")

    cursor.close()
    conexao.close()