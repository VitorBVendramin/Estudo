def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")
    if len(cpf) != 11:
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