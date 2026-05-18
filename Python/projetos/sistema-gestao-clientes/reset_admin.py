import hashlib
from database.database import conectar

# Essa função é caso o master esqueça a senha e precise resetar ela, como é um projeto somente meu, não fiz verificação por email ou algo do genero mas achei interessante implementar essa função aqui
def resetar_senha_master():
    nova_senha = input("Digite a nova senha do master: ")
    senha_hash = hashlib.sha256(nova_senha.encode()).hexdigest()
    
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE usuarios SET senha = ? WHERE cargo = 'master'", (senha_hash,))
    conexao.commit()
    
    print("Senha resetada com sucesso!")
    cursor.close()
    conexao.close()

resetar_senha_master()