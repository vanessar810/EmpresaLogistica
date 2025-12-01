import pytest
from app.service.cliente_service import ClienteService
from app.entity.cliente import Cliente
from app.exception.http_exceptions import invalid_data_error


class FakeClienteRepository:
    """Simula el repositorio sin depender de la base de datos real."""

    data = {}

    @classmethod
    def create(cls, db, cliente):
        cls.data[cliente.email] = cliente
        return cliente

    @classmethod
    def get_by_id(cls, db, cliente_id):
        for c in cls.data.values():
            if c.id == cliente_id:
                return c
        return None

    @classmethod
    def get_all(cls, db, skip, limit, nombre):
        return list(cls.data.values())

    @classmethod
    def update(cls, db, cliente):
        cls.data[cliente.email] = cliente
        return cliente

    @classmethod
    def delete(cls, db, cliente):
        del cls.data[cliente.email]


def test_create_cliente_ok(monkeypatch, db_session):
    monkeypatch.setattr(
        "app.service.cliente_service.ClienteRepository", FakeClienteRepository
    )
    class FakeCliente:
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)

    monkeypatch.setattr("app.service.cliente_service.Cliente", FakeCliente)


    cliente = ClienteService.create_cliente(
        db_session, "Vanessa", "vanessa@test.com", "1234567"
    )
    assert cliente.nombre == "Vanessa"
    assert cliente.email == "vanessa@test.com"


def test_create_cliente_sin_nombre(monkeypatch, db_session):
    monkeypatch.setattr(
        "app.service.cliente_service.ClienteRepository", FakeClienteRepository
    )
    with pytest.raises(Exception) as exc:
        ClienteService.create_cliente(db_session, "", "email@test.com", "123")
    # ✅ ahora el mensaje correcto es el de validación (422)
    assert "El nombre y el correo son obligatorios" in str(exc.value)
