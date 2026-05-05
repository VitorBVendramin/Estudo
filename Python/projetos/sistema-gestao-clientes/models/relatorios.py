from database.database import conectar

def vendas_por_periodo():

def historico_por_cliente():

def produtos_estoque_baixo():

def faturamento_total():

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT SUM(valor) FROM vendas")
    resultado = cursor.fetchone()
    print(f"Faturamento total: R${resultado[0]:.2f}")