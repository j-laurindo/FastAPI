from pydantic.v1 import BaseSettings
from sqlalchemy.orm import declarative_base

class Settings(BaseSettings):
    # URL do API + Versão
    API_V1_STR: str = "/api/v1"

    # URL do banco de dados conectado ao xampp
    DB_URL: str = "mysql+asyncmy://root@127.0.0.1:3306/btc"

    DBBaseModel = declarative_base()

class Config:
    case_sensitive = False
    env_file = "env"

settings = Settings()