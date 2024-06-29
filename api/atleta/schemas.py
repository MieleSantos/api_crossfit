from typing import Annotated

from pydantic import Field, PositiveFloat
from contrib.schemas import BaseSchema


class Atleta(BaseSchema):
    nome: Annotated[
        str, Field(description="Nome do atleta", examples="Joao", max_length=50)
    ]
    cpf: Annotated[
        str, Field(description="Cpf do atleta", examples="00000000000", max_length=11)
    ]
    idade: Annotated[int, Field(description="idade do atleta", examples=18)]
    peso: Annotated[PositiveFloat, Field(description="Peso do Atleta", examples=76.9)]
    altura: Annotated[
        PositiveFloat, Field(description="Altura do atleta", examples=1.70)
    ]
    sexo: Annotated[
        str, Field(description="Sexo do atleta", examples="M", max_length=1)
    ]
