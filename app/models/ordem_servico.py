from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database.base import Base


class OrdemServico(Base):
    __tablename__ = "ordens_servico"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    descricao = Column(String(1000))
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=True)
    empresa_id = Column(Integer, ForeignKey("empresas.id"), nullable=True)
    status = Column(String(32), default="aberta")
    created_at = Column(DateTime, default=datetime.utcnow)
