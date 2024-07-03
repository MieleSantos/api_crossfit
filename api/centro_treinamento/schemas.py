from typing import Annotated

from pydantic import UUID4, Field

from api.contrib.schemas import BaseSchema


class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[
        str,
        Field(
            description="Nome do centro de treinamento",
            example="Ct King",
            max_length=20,
        ),
    ]

    endereco: Annotated[
        str,
        Field(
            description="Endereco do centro de treinamento",
            example="rua do teste",
            max_length=60,
        ),
    ]
    proprietario: Annotated[
        str,
        Field(
            description="Dono do centro de treinamento", example="Joao", max_length=60
        ),
    ]


class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[
        str,
        Field(
            description="Nome do centro de treinamento",
            example="Ct King",
            max_length=20,
        ),
    ]


class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description="Identificador da categoria")]
