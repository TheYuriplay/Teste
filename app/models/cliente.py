from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database.base import Base


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    email = Column(String(120))
    phone = Column(String(32))
    empresa_id = Column(Integer, ForeignKey("empresas.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
