from uuid import uuid4
from fastapi import APIRouter, Body, status
from api.categoria.schemas import CategoriaIn, CategoriaOut
from api.categoria.models import CategoriaModel

from api.contrib.dependencies import data_base_dependecy

router = APIRouter()


@router.post(
    "/",
    summary="Criar uma nova categoria",
    status_code=status.HTTP_201_CREATED,
    response_model=CategoriaOut,
)
async def post(db_session: data_base_dependecy, categoria_in: CategoriaIn = Body(...)):
    categoria_out = CategoriaOut(id=uuid4(), **categoria_in.model_dump())
    categoria_model = CategoriaModel(**categoria_out.model_dump())
    db_session.add(categoria_model)
    await db_session.commit()
    return categoria_out
