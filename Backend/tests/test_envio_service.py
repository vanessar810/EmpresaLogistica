import pytest
from app.service.envio_service import EnvioService


class FakeEnvioRepository:
    data = []

    @classmethod
    def create(cls, db, envio):
        cls.data.append(envio)
        return envio

    @classmethod
    def get_by_id(cls, db, model, id):
        for e in cls.data:
            if getattr(e, "id", None) == id:
                return e
        return None

    @classmethod
    def get_all(cls, db, model, skip, limit, tipo_producto, cliente_id):
        return cls.data

    @classmethod
    def delete(cls, db, envio):
        cls.data.remove(envio)

    @classmethod
    def update(cls, db, envio):
        return envio


def test_crear_envio_terrestre_descuento(monkeypatch, db_session):
    # Mockea dependencias
    monkeypatch.setattr("app.service.envio_service.EnvioRepository", FakeEnvioRepository)
    monkeypatch.setattr("app.service.envio_service.validar_placa", lambda x: True)

    # ✅ Mockea la clase EnvioTerrestre
    class FakeEnvioTerrestre:
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)

    monkeypatch.setattr("app.service.envio_service.EnvioTerrestre", FakeEnvioTerrestre)

    data = {
        "tipo_producto": "Electrónicos",
        "cantidad": 15,
        "fecha_registro": "2025-12-01",
        "fecha_entrega": "2025-12-05",
        "bodega_entrega": "Bodega A",
        "precio_envio": 1000.0,
        "placa": "ABC123",
        "numero_guia": "G12345",
        "cliente_id": 1
    }

    envio = EnvioService.crear_envio_terrestre(db_session, data)
    assert envio.descuento == 50.0  # 5% de 1000
    assert envio.tipo_producto == "Electrónicos"
    assert envio.placa == "ABC123"


def test_crear_envio_maritimo_descuento(monkeypatch, db_session):
    # Mockea dependencias
    monkeypatch.setattr("app.service.envio_service.EnvioRepository", FakeEnvioRepository)
    monkeypatch.setattr("app.service.envio_service.validar_numero_flota", lambda x: True)

    # ✅ Mockea la clase EnvioMaritimo
    class FakeEnvioMaritimo:
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)

    monkeypatch.setattr("app.service.envio_service.EnvioMaritimo", FakeEnvioMaritimo)

    data = {
        "tipo_producto": "Alimentos",
        "cantidad": 20,
        "fecha_registro": "2025-12-01",
        "fecha_entrega": "2025-12-10",
        "puerto_entrega": "Cartagena",
        "precio_envio": 2000.0,
        "numero_flota": "F12345",
        "numero_guia": "G54321",
        "cliente_id": 1
    }

    envio = EnvioService.crear_envio_maritimo(db_session, data)
    assert envio.descuento == 60.0  # 3% de 2000
    assert envio.tipo_producto == "Alimentos"
    assert envio.numero_flota == "F12345"