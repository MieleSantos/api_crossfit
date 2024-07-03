from fastapi import APIRouter, Body, status, HTTPException
from uuid import uuid4
from pydantic import UUID4
from datetime import datetime
from api.atleta.schemas import AtletaIn, AtletaOut
from api.contrib.dependencies import data_base_dependecy
from sqlalchemy.future import select
from api.atleta.models import AtletaModel
from api.categoria.models import CategoriaModel
from api.centro_treinamento.models import CentroTreinamentoModel

router = APIRouter()


@router.get(
    "/",
    summary="Consultar todos os atletas",
    status_code=status.HTTP_200_OK,
    response_model=list[AtletaOut],
)
async def get_atletas(db_sesseion: data_base_dependecy) -> list[AtletaOut]:
    atleta_out: list[AtletaOut] = (
        (await db_sesseion.execute(select(AtletaModel))).scalars().all()
    )
    return atleta_out


@router.get(
    "/{id}",
    summary="Consultar um atleta pelo Id",
    status_code=status.HTTP_200_OK,
    response_model=AtletaOut,
)
async def get_atleta(id: UUID4, db_sesseion: data_base_dependecy) -> AtletaOut:
    atleta_out: AtletaOut = (
        (await db_sesseion.execute(select(AtletaModel).filter_by(id=id)))
        .scalars()
        .first()
    )
    if not atleta_out:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Atleta não encontrado!"
        )
    return atleta_out


@router.post(
    "/",
    summary="Criar novo atleta",
    status_code=status.HTTP_201_CREATED,
    response_model=AtletaOut,
)
async def post(db_session: data_base_dependecy, atleta_in: AtletaIn = Body(...)):

    categoria_nome = atleta_in.categoria.nome
    centro_treinamento_nome = atleta_in.centro_treinamento.nome
    categoria = (
        (
            await db_session.execute(
                select(CategoriaModel).filter_by(nome=categoria_nome)
            )
        )
        .scalars()
        .first()
    )
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Categoria não encontrada!"
        )

    centro_treinamento = (
        (
            await db_session.execute(
                select(CentroTreinamentoModel).filter_by(nome=centro_treinamento_nome)
            )
        )
        .scalars()
        .first()
    )
    if not centro_treinamento:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="O centro treinamento não encontrado!",
        )
    try:
        atleta_out = AtletaOut(
            id=uuid4(), created_at=datetime.utcnow(), **atleta_in.model_dump()
        )
        atleta_model = AtletaModel(
            **atleta_out.model_dump(exclude={"categoria", "centro_treinamento"})
        )
        atleta_model.categoria_id = categoria.pk_id
        atleta_model.centro_treinamento_id = centro_treinamento.pk_id
        db_session.add(atleta_model)
        await db_session.commit()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro na inserção dos dados do banco!",
        )
    return atleta_out
