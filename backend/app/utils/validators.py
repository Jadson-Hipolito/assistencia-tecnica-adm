import re
from datetime import date
from typing import Optional


# =========================
# EMAIL
# =========================
def validar_email(email: Optional[str]) -> bool:
    if not email:
        return False

    padrao = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    return re.match(padrao, email.strip()) is not None



# =========================
# SENHA
# =========================
def validar_senha(senha: Optional[str]) -> tuple[bool, str]:

    if not senha:
        return False, "Senha obrigatória"

    if len(senha) < 6:
        return False, "Senha mínima de 6 caracteres"

    if not re.search(r"[A-Z]", senha):
        return False, "Precisa de letra maiúscula"

    if not re.search(r"[a-z]", senha):
        return False, "Precisa de letra minúscula"

    if not re.search(r"\d", senha):
        return False, "Precisa de número"

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        return False, "Precisa de caractere especial"

    return True, "OK"



# =========================
# NOME
# =========================
def validar_nome(nome: Optional[str]) -> tuple[bool, str]:

    if not nome:
        return False, "Nome obrigatório"

    nome = nome.strip()

    if len(nome) < 3:
        return False, "Nome deve ter pelo menos 3 caracteres"

    if not re.match(r"^[A-Za-zÀ-ÿ\s]+$", nome):
        return False, "Nome deve conter apenas letras"

    return True, "OK"



# =========================
# TELEFONE
# =========================
def validar_telefone(telefone: Optional[str]) -> tuple[bool, str]:

    if not telefone:
        return False, "Telefone obrigatório"

    tel = re.sub(r"\D", "", telefone)

    if len(tel) not in (10, 11):
        return False, "Telefone inválido (DDD + número)"

    return True, "OK"



# =========================
# CPF
# =========================
def validar_cpf(cpf: Optional[str]) -> tuple[bool, str]:

    if not cpf:
        return False, "CPF obrigatório"

    cpf = re.sub(r"\D", "", cpf)

    if len(cpf) != 11:
        return False, "CPF deve ter 11 dígitos"

    if cpf == cpf[0] * 11:
        return False, "CPF inválido"


    soma = sum(
        int(cpf[i]) * (10 - i)
        for i in range(9)
    )

    dig1 = (soma * 10 % 11) % 10


    soma = sum(
        int(cpf[i]) * (11 - i)
        for i in range(10)
    )

    dig2 = (soma * 10 % 11) % 10


    if dig1 != int(cpf[9]) or dig2 != int(cpf[10]):
        return False, "CPF inválido"


    return True, "OK"



# =========================
# CNPJ
# =========================
def validar_cnpj(cnpj: Optional[str]) -> tuple[bool, str]:

    if not cnpj:
        return False, "CNPJ obrigatório"


    cnpj = re.sub(r"\D", "", cnpj)


    if len(cnpj) != 14:
        return False, "CNPJ deve ter 14 dígitos"


    if cnpj == cnpj[0] * 14:
        return False, "CNPJ inválido"


    def calcular(numero, pesos):

        soma = sum(
            int(n) * p
            for n, p in zip(numero, pesos)
        )

        resto = soma % 11

        return 0 if resto < 2 else 11 - resto


    pesos1 = [
        5,4,3,2,
        9,8,7,6,
        5,4,3,2
    ]

    dig1 = calcular(cnpj[:12], pesos1)


    pesos2 = [
        6,5,4,3,
        2,9,8,7,
        6,5,4,3,
        2
    ]

    dig2 = calcular(
        cnpj[:12] + str(dig1),
        pesos2
    )


    if cnpj[-2:] != f"{dig1}{dig2}":
        return False, "CNPJ inválido"


    return True, "OK"



# =========================
# DOCUMENTO
# =========================
def validar_documento(tipo: str, documento: str):

    if not tipo:
        return False, "Tipo inválido"


    tipo = tipo.strip().lower()


    if tipo == "fisica":
        return validar_cpf(documento)


    if tipo == "juridica":
        return validar_cnpj(documento)


    return False, "Tipo de pessoa inválido"



# =========================
# ENDEREÇO
# =========================
def validar_endereco(endereco: Optional[str]):

    if not endereco:
        return False, "Endereço obrigatório"


    if len(endereco.strip()) < 5:
        return False, "Endereço muito curto"


    return True, "OK"



# =========================
# STATUS
# =========================
def validar_status(status, opcoes):

    if status not in opcoes:
        return False, f"Status inválido. Use: {opcoes}"


    return True, "OK"



# =========================
# VALOR
# =========================
def validar_valor(valor):

    if valor is None:
        return False, "Valor obrigatório"


    try:
        valor = float(valor)

    except ValueError:
        return False, "Valor inválido"


    if valor <= 0:
        return False, "Valor deve ser maior que zero"


    return True, "OK"



# =========================
# DATA
# =========================
def validar_data(data: Optional[date]):

    if data is None:
        return False, "Data inválida"


    return True, "OK"



# =========================
# ID
# =========================
def validar_id(id_val):

    if id_val is None:
        return False, "ID obrigatório"


    if isinstance(id_val, bool):
        return False, "ID inválido"


    if not isinstance(id_val, int):
        return False, "ID deve ser inteiro"


    if id_val <= 0:
        return False, "ID deve ser maior que zero"


    return True, "OK"



# =========================
# CÓDIGO
# =========================
def validar_codigo_generico(codigo: Optional[str]):

    if not codigo:
        return False, "Código obrigatório"


    codigo = codigo.strip()


    if len(codigo) < 3:
        return False, "Código muito curto"


    if len(codigo) > 20:
        return False, "Código muito longo"


    if not re.match(r"^[A-Za-z0-9-]+$", codigo):
        return False, "Código contém caracteres inválidos"


    return True, "OK"