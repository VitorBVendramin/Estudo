def validar_cpf(cpf):
    # verifica formato exato 000.000.000-00
    if len(cpf) != 14:
        return False
    if cpf[3] != "." or cpf[7] != "." or cpf[11] != "-":
        return False
    
    cpf = cpf.replace(".", "").replace("-", "")
    if len(cpf) != 11:
        return False
    if not cpf.isdigit():  # verifica se todos os caracteres são números
        return False
    if len(set(cpf)) == 1:
        return False
    
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9)) # valida primeiro dígito verificador
    digito1 = (soma * 10 % 11) % 10
    if digito1 != int(cpf[9]):
        return False
    
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10)) # valida segundo dígito verificador
    digito2 = (soma * 10 % 11) % 10
    if digito2 != int(cpf[10]):
        return False
    
    return True

def validar_email(email):
    if "@" not in email or "." not in email:
        return False
    return True

def validar_telefone(telefone):
    telefone = telefone.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
    if len(telefone) < 10 or len(telefone) > 11:
        return False
    return True