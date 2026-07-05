from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from app.database.base import Base


class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    cnpj = Column(String(32), unique=True)
    address = Column(String(250))
    created_at = Column(DateTime, default=datetime.utcnow)
