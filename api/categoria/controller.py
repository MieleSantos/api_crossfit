from uuid import uuid4

from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy.future import select

from api.categoria.models import CategoriaModel
from api.categoria.schemas import CategoriaIn, CategoriaOut
from api.contrib.dependencies import data_base_dependecy

router = APIRouter()


@router.get(
    "/",
    summary="Consultar todas as Categorias",
    status_code=status.HTTP_200_OK,
    response_model=list[CategoriaOut],
)
async def get_categoria(db_sesseion: data_base_dependecy) -> list[CategoriaOut]:
    categorias: list[CategoriaOut] = (
        (await db_sesseion.execute(select(CategoriaModel))).scalars().all()
    )
    return categorias


@router.get(
    "/{id}",
    summary="Consultar uma Categoria pelo Id",
    status_code=status.HTTP_200_OK,
    response_model=CategoriaOut,
)
async def get_categoria(id: UUID4, db_sesseion: data_base_dependecy) -> CategoriaOut:
    categoria: CategoriaOut = (
        (await db_sesseion.execute(select(CategoriaModel).filter_by(id=id)))
        .scalars()
        .first()
    )
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Categoria não encontrada!"
        )
    return categoria


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
