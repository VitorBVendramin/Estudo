from database.database import conectar

def cadastrar_cliente():

    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    cpf = input("CPF: ")
    endereco = input("Endereço: ")
    
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO clientes (nome, email, telefone, cpf, endereco)
        VALUES (?, ?, ?, ?, ?)""
    """, (nome, email, telefone, cpf, endereco))
    
    conexao.commit()
    print("Cliente cadastrado com sucesso!")

def buscar_todos():

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    for cliente in clientes:
        print(cliente)

def buscar_por_nome():

    nome = input("Digite o nome do cliente: ")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes WHERE nome = ?", (nome,))
    clientes = cursor.fetchall()
    
    for cliente in clientes:
        print(cliente)

def buscar_por_id():

    id = int(input("Digite o id do cliente: "))
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes WHERE id = ?", (id,))
    cliente = cursor.fetchone()
    
    print(cliente)

def atualizar_cliente():

    id = int(input("Digite o id do cliente: "))
    
    print("O que deseja atualizar?")
    print("1 - Nome")
    print("2 - Email")
    print("3 - Telefone")
    print("4 - CPF")
    print("5 - Endereço")
    
    opcao = int(input("Escolha: "))
    
    if opcao == 1:
        novo_valor = input("Novo nome: ")
        campo = "nome"
    elif opcao == 2:
        novo_valor = input("Novo email: ")
        campo = "email"
    elif opcao == 3:
        novo_valor = input("Novo telefone: ")
        campo = "telefone"
    elif opcao == 4:
        novo_valor = input("Novo cpf: ")
        campo = "cpf"
    elif opcao == 5:
        novo_valor = input("Novo endereço: ")
        campo = "endereco"
    
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(f"UPDATE clientes SET {campo} = ? WHERE id = ?", (novo_valor, id))
    conexao.commit()

    print("Cliente atualizado com sucesso!")

def deletar_cliente():

    id = int(input("Digite o id do cliente que deseja deletar: "))
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = ?", (id,))
    conexao.commit()
    
    print("Cliente deletado com sucesso!")