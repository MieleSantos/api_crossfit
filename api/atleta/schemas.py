from typing import Annotated

from pydantic import Field, PositiveFloat

from api.categoria.schemas import CategoriaIn
from api.centro_treinamento.schemas import CentroTreinamentoAtleta
from api.contrib.schemas import BaseSchema, OutMixin


class Atleta(BaseSchema):
    nome: Annotated[
        str, Field(description="Nome do atleta", example="Joao", max_length=50)
    ]
    cpf: Annotated[
        str, Field(description="Cpf do atleta", example="00000000000", max_length=11)
    ]
    idade: Annotated[int, Field(description="idade do atleta", example=18)]
    peso: Annotated[PositiveFloat, Field(description="Peso do Atleta", example=76.9)]
    altura: Annotated[
        PositiveFloat, Field(description="Altura do atleta", example=1.70)
    ]
    sexo: Annotated[str, Field(description="Sexo do atleta", example="M", max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description="Categoria do atleta")]
    centro_treinamento: Annotated[
        CentroTreinamentoAtleta, Field(description="Centro de treinamento do atleta")
    ]


class AtletaIn(Atleta):
    pass


class AtletaOut(Atleta, OutMixin):
    pass
