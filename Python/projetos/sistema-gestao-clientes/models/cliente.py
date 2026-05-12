from database.database import conectar
from datetime import datetime
from validacoes import validar_cpf, validar_email, validar_telefone

def cadastrar_cliente():

    nome = input("Nome: ")

    while True:
        email = input("Email: ")
        if validar_email(email):
            break
        else:
            print("Email inválido! Digite novamente.")

    while True:
        telefone = input("Telefone: ")
        if validar_telefone(telefone):
            break
        else:
            print("telefone inválido! Digite novamente.")

    while True:
        cpf = input("CPF: ")
        if validar_cpf(cpf):
            break
        else:
            print("CPF inválido! Digite novamente.")

    endereco = input("Endereço: ")

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO clientes (nome, email, telefone, cpf, endereco)
        VALUES (?, ?, ?, ?, ?)
    """, (nome, email, telefone, cpf, endereco))
    
    conexao.commit()
    print("Cliente cadastrado com sucesso!")

    cursor.close()
    conexao.close()

def buscar_todos():

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall() # fetchall retorna todos os resultados encontrados

    if not clientes:
        print("Não existe cliente cadastrado.")
    else:
        print("\n=== CLIENTES CADASTRADOS ===")

        for cliente in clientes:
            print(f"""
ID: {cliente[0]}
Nome: {cliente[1]}
Email: {cliente[2]}
Telefone: {cliente[3]}
CPF: {cliente[4]}
Endereço: {cliente[5]}
------------------------
""")


    cursor.close()
    conexao.close()

def buscar_por_nome():

    nome = input("Digite o nome do cliente: ")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes WHERE nome = ?", (nome,))
    clientes = cursor.fetchall()

    if not clientes:
        print("Nenhum cliente encontrado com esse nome.")
    else:
        print("\n=== CLIENTES ENCONTRADOS ===")

        for cliente in clientes:
            print(f"""
ID: {cliente[0]}
Nome: {cliente[1]}
Email: {cliente[2]}
Telefone: {cliente[3]}
CPF: {cliente[4]}
Endereço: {cliente[5]}
------------------------
""")

    cursor.close()
    conexao.close()

def buscar_por_id():

    cliente_id = int(input("Digite o id do cliente: "))
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes WHERE id = ?", (cliente_id,))
    cliente = cursor.fetchone() # fetchone retorna apenas um registro — ideal para busca por id único

    if not cliente:
        print("ID não encontrado.")
    else:
        print("\n=== CLIENTE CADASTRADO ===")
        print(f"""
ID: {cliente[0]}
Nome: {cliente[1]}
Email: {cliente[2]}
Telefone: {cliente[3]}
CPF: {cliente[4]}
Endereço: {cliente[5]}
------------------------
""")

    cursor.close()
    conexao.close()

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
    cursor.execute(f"UPDATE clientes SET {campo} = ? WHERE id = ?", (novo_valor, id)) # monta o SQL dinamicamente com o campo escolhido pelo usuário
    conexao.commit()

    print("Cliente atualizado com sucesso!")

    cursor.close()
    conexao.close()

def deletar_cliente():

    id = int(input("Digite o id do cliente que deseja deletar: "))
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = ?", (id,))
    conexao.commit()
    
    print("Cliente deletado com sucesso!")

    cursor.close()
    conexao.close()