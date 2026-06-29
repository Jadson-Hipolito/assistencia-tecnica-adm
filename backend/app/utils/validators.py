import re


# =========================
# EMAIL
# =========================
def validar_email(email: str) -> bool:
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao, email) is not None


# =========================
# SENHA
# =========================
def validar_senha(senha: str) -> tuple[bool, str]:
    if len(senha) < 6:
        return False, "Senha mínima de 6 caracteres"

    if not re.search(r"[A-Z]", senha):
        return False, "Precisa de letra maiúscula"

    if not re.search(r"[a-z]", senha):
        return False, "Precisa de letra minúscula"

    if not re.search(r"[0-9]", senha):
        return False, "Precisa de número"

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        return False, "Precisa de caractere especial"

    return True, "OK"


# =========================
# NOME
# =========================
def validar_nome(nome: str) -> tuple[bool, str]:
    if len(nome.strip()) < 3:
        return False, "Nome deve ter pelo menos 3 caracteres"

    if not re.match(r"^[A-Za-zÀ-ÿ\s]+$", nome):
        return False, "Nome deve conter apenas letras"

    return True, "OK"


# =========================
# TELEFONE / CONTATO (BR)
# =========================
def validar_telefone(telefone: str) -> tuple[bool, str]:
    # Remove espaços, traços, parênteses
    tel = re.sub(r"\D", "", telefone)

    if len(tel) not in [10, 11]:
        return False, "Telefone inválido (use DDD + número)"

    return True, "OK"


# =========================
# CPF
# =========================
def validar_cpf(cpf: str) -> tuple[bool, str]:
    cpf = re.sub(r"\D", "", cpf)

    if len(cpf) != 11:
        return False, "CPF deve ter 11 dígitos"

    if cpf == cpf[0] * 11:
        return False, "CPF inválido"

    # validação básica dos dígitos verificadores
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    dig1 = (soma * 10 % 11) % 10

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    dig2 = (soma * 10 % 11) % 10

    if dig1 != int(cpf[9]) or dig2 != int(cpf[10]):
        return False, "CPF inválido"

    return True, "OK"


# =========================
# CNPJ
# =========================
def validar_cnpj(cnpj: str) -> tuple[bool, str]:
    cnpj = re.sub(r"\D", "", cnpj)

    if len(cnpj) != 14:
        return False, "CNPJ deve ter 14 dígitos"

    if cnpj == cnpj[0] * 14:
        return False, "CNPJ inválido"

    def calc_digito(cnpj, pesos):
        soma = sum(int(num) * peso for num, peso in zip(cnpj, pesos))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    pesos1 = [5,4,3,2,9,8,7,6,5,4,3,2]
    dig1 = calc_digito(cnpj[:12], pesos1)

    pesos2 = [6] + pesos1
    dig2 = calc_digito(cnpj[:12] + str(dig1), pesos2)

    if cnpj[-2:] != f"{dig1}{dig2}":
        return False, "CNPJ inválido"

    return True, "OK"

def validar_documento(tipo: str, documento: str) -> tuple[bool, str]:
    if tipo.lower() == "fisica":
        return validar_cpf(documento)

    if tipo.lower() == "juridica":
        return validar_cnpj(documento)

    return False, "Tipo de pessoa inválido"

def validar_endereco(endereco: str) -> tuple[bool, str]:
    if len(endereco.strip()) < 5:
        return False, "Endereço muito curto"

    return True, "OK"

def validar_status(status: str, opcoes: list) -> tuple[bool, str]:
    if status not in opcoes:
        return False, f"Status inválido. Use: {opcoes}"

    return True, "OK"

def validar_valor(valor: float) -> tuple[bool, str]:
    if valor <= 0:
        return False, "Valor deve ser maior que zero"

    return True, "OK"

from datetime import date

def validar_data(data: date) -> tuple[bool, str]:
    if data is None:
        return False, "Data inválida"

    return True, "OK"

def validar_id(id_val: int) -> tuple[bool, str]:
    if id_val is None:
        return False, "ID não pode ser nulo"

    if not isinstance(id_val, int):
        return False, "ID deve ser um número inteiro"

    if id_val <= 0:
        return False, "ID deve ser maior que zero"

    return True, "OK"

def validar_codigo_generico(codigo: str) -> tuple[bool, str]:
    if not codigo:
        return False, "Código não pode ser vazio"

    codigo = codigo.strip()

    if len(codigo) < 3:
        return False, "Código muito curto"

    if len(codigo) > 20:
        return False, "Código muito longo"

    # aceita letras, números e hífen
    padrao = r'^[A-Za-z0-9\-]+$'

    if not re.match(padrao, codigo):
        return False, "Código contém caracteres inválidos"

    return True, "OK"