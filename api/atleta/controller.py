from fastapi import APIRouter, Body, status
from uuid import uuid4
from api.atleta.schemas import AtletaIn, AtletaOut
from api.contrib.dependencies import data_base_dependecy
from api.atleta.models import AtletaModel

router = APIRouter()


@router.post(
    "/",
    summary="Criar novo atleta",
    status_code=status.HTTP_201_CREATED,
    response_model=AtletaOut,
)
async def post(db_session: data_base_dependecy, atleta_in: AtletaIn = Body(...)):
    atleta_out = AtletaOut(id=uuid4(), **atleta_in.model_dump())
    atleta_model = AtletaModel(**atleta_out.model_dump())
    db_session.add(atleta_model)
    await db_session.commit()
    return atleta_out
