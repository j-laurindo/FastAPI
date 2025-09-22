from fastapi import APIRouter
from api.v1.endpoints import turmas

api_router = APIRouter()

api_router.include_router(turmas.router, prefix="/turmas", tags=["Essa é a parte de turmas"])