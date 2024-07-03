from uuid import uuid4
from fastapi import APIRouter, Body, status, HTTPException
from sqlalchemy.future import select
from pydantic import UUID4
from api.centro_treinamento.schemas import (
    CentroTreinamentoIn,
    CentroTreinamentoOut,
)
from api.centro_treinamento.models import CentroTreinamentoModel
from api.contrib.dependencies import data_base_dependecy

router = APIRouter()


@router.get(
    "/",
    summary="Consultar todos os Centro de treinamento",
    status_code=status.HTTP_200_OK,
    response_model=list[CentroTreinamentoOut],
)
async def get_categoria(db_sesseion: data_base_dependecy) -> list[CentroTreinamentoOut]:
    categorias: list[CentroTreinamentoOut] = (
        (await db_sesseion.execute(select(CentroTreinamentoModel))).scalars().all()
    )
    return categorias


@router.get(
    "/{id}",
    summary="Consultar um Centro de treinamento pelo Id",
    status_code=status.HTTP_200_OK,
    response_model=CentroTreinamentoOut,
)
async def get_categoria(
    id: UUID4, db_sesseion: data_base_dependecy
) -> CentroTreinamentoOut:
    categoria: CentroTreinamentoOut = (
        (await db_sesseion.execute(select(CentroTreinamentoModel).filter_by(id=id)))
        .scalars()
        .first()
    )
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Centro de treinamento não encontrada!",
        )
    return categoria


@router.post(
    "/",
    summary="Criar um novo Centro de treinamento",
    status_code=status.HTTP_201_CREATED,
    response_model=CentroTreinamentoOut,
)
async def create_centro(
    db_session: data_base_dependecy, centro_treino_in: CentroTreinamentoIn = Body(...)
) -> CentroTreinamentoOut:
    try:
        centro_treino_out = CentroTreinamentoOut(
            id=uuid4(), **centro_treino_in.model_dump()
        )
        centro_treino_model = CentroTreinamentoModel(**centro_treino_out.model_dump())
        db_session.add(centro_treino_model)
        await db_session.commit()
    except Exception as e:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    return centro_treino_out
