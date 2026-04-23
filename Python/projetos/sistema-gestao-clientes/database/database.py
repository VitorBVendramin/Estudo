import sqlite3

def conectar():
    conexao = sqlite3.connect("database/banco.db")
    return conexao

def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT,
        telefone TEXT,
        cpf TEXT,
        endereco TEXT
    )
""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER,
        produto_id INTEGER,
        quantidade INTEGER,
        valor REAL,
        data TEXT,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        FOREIGN KEY (produto_id) REFERENCES produtos(id)
    )
""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        preco REAL NOT NULL
    )
""")


    conexao.commit()

criar_tabelas()