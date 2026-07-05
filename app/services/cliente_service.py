from typing import List, Optional
from app.database.connection import get_session
from app.models.cliente import Cliente


def list_all() -> List[Cliente]:
    session = get_session()
    try:
        return session.query(Cliente).order_by(Cliente.name).all()
    finally:
        session.close()


def get_by_id(cliente_id: int) -> Optional[Cliente]:
    session = get_session()
    try:
        return session.query(Cliente).get(cliente_id)
    finally:
        session.close()


def create(data: dict) -> Cliente:
    session = get_session()
    try:
        cliente = Cliente(**data)
        session.add(cliente)
        session.commit()
        session.refresh(cliente)
        return cliente
    finally:
        session.close()


def update(cliente_id: int, data: dict) -> Optional[Cliente]:
    session = get_session()
    try:
        cliente = session.query(Cliente).get(cliente_id)
        if not cliente:
            return None
        for k, v in data.items():
            setattr(cliente, k, v)
        session.add(cliente)
        session.commit()
        session.refresh(cliente)
        return cliente
    finally:
        session.close()


def delete(cliente_id: int) -> bool:
    session = get_session()
    try:
        cliente = session.query(Cliente).get(cliente_id)
        if not cliente:
            return False
        session.delete(cliente)
        session.commit()
        return True
    finally:
        session.close()
