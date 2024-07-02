from fastapi import APIRouter, Body, status

from api.atleta.schemas import AtletaIn, AtletaOut
from api.contrib.dependencies import data_base_dependecy

router = APIRouter()


@router.post(
    "/",
    summary="Criar novo atleta",
    status_code=status.HTTP_201_CREATED,
    response_model=AtletaOut,
)
async def post(db_session: data_base_dependecy, atleta: AtletaIn = Body(...)):
    pass
