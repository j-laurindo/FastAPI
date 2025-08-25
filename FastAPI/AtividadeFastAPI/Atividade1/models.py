from typing import Optional
from pydantic import BaseModel

class PersonagensUrsinhoPooh(BaseModel):
    id: Optional[int] = None
    nome: str
    raca: str
    traco: str
    filmes: str
    foto: str

class filmesUrsinhoPooh(BaseModel):
    id: Optional[int] = None
    titulo: str
    data_lancamento: int
    sinopse: str
    genero: str