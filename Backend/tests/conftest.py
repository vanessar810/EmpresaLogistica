# tests/conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from app.configuration.database import Base

from app.entity import cliente, envio_maritimo, envio_terrestre, user

@pytest.fixture(scope="function")
def db_session():
    """Crea una sesión de base de datos temporal en memoria."""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    SessionTesting = sessionmaker(bind=engine)
    session = SessionTesting()

    yield session

    session.close()
    clear_mappers()