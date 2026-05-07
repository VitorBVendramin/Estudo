from database.database import conectar
from datetime import datetime

def vendas_por_periodo():

    data_inicial = input("Digite a data inicial: ")
    data_final = input("Digite a data final: ")

    sql = """
    SELECT COUNT(*), SUM(valor)
    FROM vendas
    WHERE data BETWEEN ? AND ?
"""

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(sql, (data_inicial, data_final))
    resultado = cursor.fetchone()
    total = resultado[1] if resultado[1] is not None else 0
    print(f"Valor total: R${total:.2f}")

    cursor.close()
    conexao.close()
    
def historico_por_cliente(): # Histórico do que cada cliente comprou, e tem abreviação no banco, V = Vendas/ P = Produtos

    cliente_id = int(input("ID do cliente: "))

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT v.id, p.nome, v.quantidade, v.valor, v.data
        FROM vendas v
        join produtos p ON v.produto_id = p.id
        WHERE v.cliente_id = ?
    """, (cliente_id,))
    cliente = cursor.fetchall()

    for venda in cliente:
        print(venda)

    cursor.close()
    conexao.close()

def produtos_estoque_baixo():

    
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT * FROM produtos
        WHERE quantidade <= 5
    """)

    produtos = cursor.fetchall()

    if not produtos:
        print("Nenhum produto com estoque baixo.")

    else:
        print("=== PRODUTOS COM ESTOQUE BAIXO ===")

        for produto in produtos:
            print(f"""
Produto: {produto[1]}
Estoque restante: {produto[2]}
""")

    cursor.close()
    conexao.close()

def faturamento_total():

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT SUM(valor) FROM vendas")
    resultado = cursor.fetchone()
    total = resultado[0] if resultado[0] is not None else 0
    print(f"Faturamento total: R${total:.2f}")

    cursor.close()
    conexao.close()