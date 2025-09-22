from typing import Optional
from pydantic import BaseModel as SCBaseModel

class TurmaSchema(SCBaseModel):

    id: Optional[int] = None
    nome_turma: str
    padrinho: str
    qtd_alunos: int
    laboratorio: str

    class Config:
        orm_mode = True