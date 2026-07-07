from datetime import date

from backend.app.utils.validators import (
    validar_email,
    validar_senha,
    validar_nome,
    validar_telefone,
    validar_cpf,
    validar_cnpj,
    validar_documento,
    validar_endereco,
    validar_status,
    validar_valor,
    validar_data,
    validar_id,
    validar_codigo_generico,
)


def test_validar_email():
    assert validar_email("teste@email.com") is True
    assert validar_email("email_invalido") is False


def test_validar_senha():
    assert validar_senha("Senha123@")[0] is True
    assert validar_senha("123")[0] is False
    assert validar_senha("senha123@")[0] is False


def test_validar_nome():
    assert validar_nome("Joao Silva")[0] is True
    assert validar_nome("A")[0] is False
    assert validar_nome("Joao123")[0] is False


def test_validar_telefone():
    assert validar_telefone("(84)99999-9999")[0] is True
    assert validar_telefone("123")[0] is False


def test_validar_cpf():
    assert validar_cpf("52998224725")[0] is True
    assert validar_cpf("11111111111")[0] is False


def test_validar_cnpj():
    assert validar_cnpj("11222333000181")[0] is True
    assert validar_cnpj("00000000000000")[0] is False


def test_validar_documento():
    assert validar_documento("fisica", "52998224725")[0] is True
    assert validar_documento("juridica", "11222333000181")[0] is True
    assert validar_documento("x", "123")[0] is False


def test_validar_endereco():
    assert validar_endereco("Rua Teste 123")[0] is True
    assert validar_endereco("a")[0] is False


def test_validar_status():
    assert validar_status("ATIVO", ["ATIVO", "INATIVO"])[0] is True
    assert validar_status("X", ["ATIVO"])[0] is False


def test_validar_valor():
    assert validar_valor(100)[0] is True
    assert validar_valor(0)[0] is False


def test_validar_data():
    assert validar_data(date.today())[0] is True
    assert validar_data(None)[0] is False


def test_validar_id():
    assert validar_id(1)[0] is True
    assert validar_id(None)[0] is False
    assert validar_id(-1)[0] is False


def test_validar_codigo_generico():
    assert validar_codigo_generico("ABC123")[0] is True
    assert validar_codigo_generico("")[0] is False
    assert validar_codigo_generico("ab@")[0] is False
