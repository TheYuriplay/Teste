from typing import List, Optional
from app.services import cliente_service


def list_clientes() -> List:
    return cliente_service.list_all()


def get_cliente(cliente_id: int):
    return cliente_service.get_by_id(cliente_id)


def create_cliente(data: dict):
    return cliente_service.create(data)


def update_cliente(cliente_id: int, data: dict):
    return cliente_service.update(cliente_id, data)


def delete_cliente(cliente_id: int):
    return cliente_service.delete(cliente_id)
