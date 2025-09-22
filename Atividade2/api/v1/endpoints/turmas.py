from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.turmas_models import TurmasModel
from schemas.turmas_schemas import TurmaSchema
from core.deps import get_session

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TurmaSchema)
async def post_turma(turma: TurmaSchema, db: AsyncSession = Depends(get_session)):
    nova_turma = TurmasModel(nome_turma = turma.nome_turma,
                             padrinho = turma.padrinho,
                             qtd_alunos = turma.qtd_alunos,
                             laboratorio = turma.laboratorio)
    
    db.add(nova_turma)
    await db.commit()

    return nova_turma

@router.get("/", response_model=List[TurmaSchema])
async def get_turmas(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(TurmasModel)
        result = await session.execute(query)
        turmas: List[TurmasModel] = result.scalars().all()

        return turmas

@router.get("/{turma_id}", response_model=TurmaSchema)
async def get_turmas(turma_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(TurmasModel).filter(TurmasModel.id == turma_id)
        result = await session.execute(query)
        turma = result.scalar_one_or_none()

        if turma:
            return turma
        else:
            raise HTTPException(detail="Turma não encontrada", status_code=status.HTTP_404_NOT_FOUND)

@router.put("/{turma_id}", response_model=TurmaSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_turma(turma_id: int, turma: TurmaSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(TurmasModel).filter(TurmasModel.id == turma_id)
        result = await session.execute(query)
        turma_up = result.scalar_one_or_none()

        if turma_up:
            turma_up.nome_turma = turma.nome_turma
            turma_up.padrinho = turma.padrinho
            turma_up.qtd_alunos = turma.qtd_alunos
            turma_up.laboratorio = turma.laboratorio

            await session.commit()
            return turma_up
        else:
            raise HTTPException(detail="Turma não encontrada", status_code=status.HTTP_404_NOT_FOUND)
        
@router.delete("/{turma_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_turma(turma_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(TurmasModel).filter(TurmasModel.id == turma_id)
        result = await session.execute(query)
        turma_del = result.scalar_one_or_none()

        if turma_del:
            await session.delete(turma_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail="Turma não encontrada", status_code=status.HTTP_404_NOT_FOUND)