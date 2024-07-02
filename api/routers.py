from fastapi import APIRouter

from api.atleta.controller import router as atleta
from api.categoria.controller import router as categoria

api_router = APIRouter()
api_router.include_router(atleta, prefix="/atletas", tags=["Atletas"])
api_router.include_router(categoria, prefix="/categoria", tags=["Categorias"])
