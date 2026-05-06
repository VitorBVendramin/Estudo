from database.database import conectar

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
    print(f"Vendas no período: {resultado[0]}")
    print(f"Valor total: R${resultado[1]:.2f}")

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
    pass

def faturamento_total():

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT SUM(valor) FROM vendas")
    resultado = cursor.fetchone()
    total = resultado[0] if resultado[0] is not None else 0
    print(f"Faturamento total: R${total:.2f}")

    cursor.close()
    conexao.close()