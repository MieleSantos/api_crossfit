from typing import Annotated

from contrib.schemas import BaseSchema
from pydantic import Field


class CentroTreinamento(BaseSchema):
    nome: Annotated[
        str,
        Field(
            description='Nome do centro de treinamento',
            example='Ct King',
            max_length=20,
        ),
    ]

    endereco: Annotated[
        str,
        Field(
            description='Endereco do centro de treinamento',
            example='rua do teste',
            max_length=60,
        ),
    ]
    proprietario: Annotated[
        str,
        Field(
            description='Dono do centro de treinamento', example='Joao', max_digits=60
        ),
    ]
