from typing import List, Optional
from app.database.connection import get_session
from app.models.ordem_servico import OrdemServico


def list_all() -> List[OrdemServico]:
    session = get_session()
    try:
        return session.query(OrdemServico).order_by(OrdemServico.created_at.desc()).all()
    finally:
        session.close()


def get_by_id(os_id: int) -> Optional[OrdemServico]:
    session = get_session()
    try:
        return session.query(OrdemServico).get(os_id)
    finally:
        session.close()


def create(data: dict) -> OrdemServico:
    session = get_session()
    try:
        os = OrdemServico(**data)
        session.add(os)
        session.commit()
        session.refresh(os)
        return os
    finally:
        session.close()


def update(os_id: int, data: dict) -> Optional[OrdemServico]:
    session = get_session()
    try:
        os = session.query(OrdemServico).get(os_id)
        if not os:
            return None
        for k, v in data.items():
            setattr(os, k, v)
        session.add(os)
        session.commit()
        session.refresh(os)
        return os
    finally:
        session.close()


def delete(os_id: int) -> bool:
    session = get_session()
    try:
        os = session.query(OrdemServico).get(os_id)
        if not os:
            return False
        session.delete(os)
        session.commit()
        return True
    finally:
        session.close()
