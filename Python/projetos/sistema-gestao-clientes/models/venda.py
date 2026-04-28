from database.database import conectar
from datetime import datetime

def registrar_venda():
    cliente_id = int(input("ID do cliente: "))
    produto_id = int(input("ID do produto: "))
    quantidade = int(input("Quantidade: "))


    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes WHERE id = ?", (cliente_id,))
    cliente = cursor.fetchone()

    if cliente is None:
        print("Cliente não encontrado!")
        return

    cursor.execute("SELECT * FROM produtos WHERE id = ?", (produto_id,))
    produto = cursor.fetchone()
    if produto is None:
        print("Produto não encontrado!")
        return
    
    if produto[2] < quantidade:
        print("Estoque insuficiente!")
        return
    
    valor = produto[3] * quantidade

    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    cursor.execute("""
    INSERT INTO vendas (cliente_id, produto_id, quantidade, valor, data)
    VALUES (?, ?, ?, ?, ?)
""", (cliente_id, produto_id, quantidade, valor, data))
    
    cursor.execute("""
    UPDATE produtos SET quantidade = quantidade - ? WHERE id = ?
""", (quantidade, produto_id))
    
    conexao.commit()
    print("Venda registrada com sucesso!")

def listar_vendas():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM vendas")
    vendas = cursor.fetchall()

    for venda in vendas:
        print(venda)

def vendas_por_cliente():
    cliente_id = int(input("ID do cliente: "))

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes WHERE id = ?", (cliente_id,))
    cliente = cursor.fetchone()

    if cliente is None:
        print("Cliente não encontrado!")
        return
    
    cursor.execute("SELECT * FROM vendas WHERE cliente_id = ?", (cliente_id,))
    vendas = cursor.fetchall()
    
    for venda in vendas:
        print(venda)

def vendas_por_produto():
    produto_id = int(input("ID do produto: "))

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos WHERE id = ?", (produto_id,))
    produto = cursor.fetchone()

    if produto is None:
        print("Produto não encontrado!")
        return
    
    cursor.execute("SELECT * FROM vendas WHERE produto_id = ?", (produto_id,))
    vendas = cursor.fetchall()
    
    for venda in vendas:
        print(venda)

def produto_mais_vendido():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT produto_id, SUM(quantidade) 
        FROM vendas 
        GROUP BY produto_id 
        ORDER BY SUM(quantidade) DESC 
        LIMIT 3
    """)

    produtos = cursor.fetchall()
    
    for produto in produtos:
        print(produto)