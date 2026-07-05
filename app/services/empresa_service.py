from typing import List, Optional
from app.database.connection import get_session
from app.models.empresa import Empresa


def list_all() -> List[Empresa]:
    session = get_session()
    try:
        return session.query(Empresa).order_by(Empresa.name).all()
    finally:
        session.close()


def get_by_id(empresa_id: int) -> Optional[Empresa]:
    session = get_session()
    try:
        return session.query(Empresa).get(empresa_id)
    finally:
        session.close()


def create(data: dict) -> Empresa:
    session = get_session()
    try:
        empresa = Empresa(**data)
        session.add(empresa)
        session.commit()
        session.refresh(empresa)
        return empresa
    finally:
        session.close()


def update(empresa_id: int, data: dict) -> Optional[Empresa]:
    session = get_session()
    try:
        empresa = session.query(Empresa).get(empresa_id)
        if not empresa:
            return None
        for k, v in data.items():
            setattr(empresa, k, v)
        session.add(empresa)
        session.commit()
        session.refresh(empresa)
        return empresa
    finally:
        session.close()


def delete(empresa_id: int) -> bool:
    session = get_session()
    try:
        empresa = session.query(Empresa).get(empresa_id)
        if not empresa:
            return False
        session.delete(empresa)
        session.commit()
        return True
    finally:
        session.close()
