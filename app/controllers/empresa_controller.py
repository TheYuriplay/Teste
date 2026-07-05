from typing import List, Optional
from app.services import empresa_service


def list_empresas() -> List:
    return empresa_service.list_all()


def get_empresa(empresa_id: int):
    return empresa_service.get_by_id(empresa_id)


def create_empresa(data: dict):
    return empresa_service.create(data)


def update_empresa(empresa_id: int, data: dict):
    return empresa_service.update(empresa_id, data)


def delete_empresa(empresa_id: int):
    return empresa_service.delete(empresa_id)
