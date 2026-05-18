import hashlib
from database.database import conectar

def criar_admin():
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("SELECT id FROM usuarios")
    usuario = cursor.fetchone()
    
    if usuario is None:
        senha = hashlib.sha256("admin0101".encode()).hexdigest()
        cursor.execute("""
            INSERT INTO usuarios (nome, login, senha, cargo)
            VALUES (?, ?, ?, ?)
        """, ("Master", "admin", senha, "master"))
        conexao.commit()
        print("Usuário master criado!")
        print("Login: admin")
        print("Senha: admin0101")
        print("Troque a senha após o primeiro acesso!")
    
    cursor.close()
    conexao.close()

def cadastrar_usuario():

    conexao = conectar()
    cursor = conexao.cursor()

    nome_usuario = input("Nome do usuario: ")
    login_usuario = (input("Login: "))
    senha_usuario = input("Senha: ")
    if not senha_usuario:
        print("Senha não pode ser vazia!")
        return
    senha_hash = hashlib.sha256(senha_usuario.encode()).hexdigest() # Transforma a senha em hash que faz uma criptografia não tem reversão, assim não fica exposto no código as senhas
    cargo = input("Cargo (master/operador/aprendiz): ")
    cursor.execute("""
        INSERT INTO usuarios (nome, login, senha, cargo)
        VALUES (?, ?, ?, ?)
    """, (nome_usuario, login_usuario, senha_hash, cargo))
    conexao.commit()

    print("Usuário cadastrado com sucesso!")

    cursor.close()
    conexao.close()

def fazer_login():

    conexao = conectar()
    cursor = conexao.cursor()

    login = input("Login: ")
    senha = input("Senha: ")
    
    # transforma a senha digitada em hash para comparar
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()
    
    # busca o usuário pelo login e senha
    cursor.execute("SELECT * FROM usuarios WHERE login = ? AND senha = ?", (login, senha_hash))
    usuario = cursor.fetchone()

    cursor.close()
    conexao.close()

    if usuario is None:
        print("Login ou senha incorretos!")
        return None
    
    print(f"Bem vindo, {usuario[1]}!")
    return usuario

def verificar_cargo():
    pass