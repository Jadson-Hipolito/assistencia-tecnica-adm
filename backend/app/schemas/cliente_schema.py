from typing import Optional

from pydantic import BaseModel, ConfigDict, field_validator

from backend.app.utils.validators import (
    validar_nome,
    validar_documento,
    validar_endereco,
    validar_telefone
)


class ClienteBase(BaseModel):

    nome: str
    documento: str  # CPF/CNPJ
    endereco: str
    contato: str
    ativo: bool = True


    @field_validator("nome")
    @classmethod
    def validar_nome_cliente(cls, valor):

        valido, mensagem = validar_nome(valor)

        if not valido:
            raise ValueError(mensagem)

        return valor



    @field_validator("documento")
    @classmethod
    def validar_documento_cliente(cls, valor):

        # Como você aceita CPF/CNPJ,
        # valida apenas se o documento possui formato correto

        documento = valor.replace(".", "").replace("-", "").replace("/", "")

        if len(documento) == 11:

            valido, mensagem = validar_documento(
                "fisica",
                documento
            )

        elif len(documento) == 14:

            valido, mensagem = validar_documento(
                "juridica",
                documento
            )

        else:
            valido = False
            mensagem = "CPF/CNPJ inválido"


        if not valido:
            raise ValueError(mensagem)

        return valor



    @field_validator("endereco")
    @classmethod
    def validar_endereco_cliente(cls, valor):

        valido, mensagem = validar_endereco(valor)

        if not valido:
            raise ValueError(mensagem)

        return valor



    @field_validator("contato")
    @classmethod
    def validar_contato_cliente(cls, valor):

        valido, mensagem = validar_telefone(valor)

        if not valido:
            raise ValueError(mensagem)

        return valor



class ClienteCreate(ClienteBase):
    pass



class ClienteUpdate(BaseModel):

    nome: Optional[str] = None
    documento: Optional[str] = None
    endereco: Optional[str] = None
    contato: Optional[str] = None
    ativo: Optional[bool] = None



class ClienteResponse(BaseModel):

    id: int
    nome: str
    documento: str | None = None
    endereco: str
    contato: str | None = None
    ativo: bool = True


    model_config = ConfigDict(
        from_attributes=True
    )