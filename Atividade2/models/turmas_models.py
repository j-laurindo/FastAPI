from core.configs import settings
from sqlalchemy import Column, Integer, String, Boolean, Float, Text

class TurmasModel(settings.DBBaseModel):
    __tablename__ = 'turmas',

    id: int = Column(Integer(), primary_key = True, autoincrement = True)
    nome_turma: str = Column(String(256))
    padrinho: str = Column(String(100))
    qtd_alunos: int = Column(Integer())
    laboratorio: str = Column(String(256))

