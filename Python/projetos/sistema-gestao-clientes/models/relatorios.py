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

def historico_por_cliente():

def produtos_estoque_baixo():

def faturamento_total():

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT SUM(valor) FROM vendas")
    resultado = cursor.fetchone()
    print(f"Faturamento total: R${resultado[0]:.2f}")