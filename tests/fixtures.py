from typing import Generator

import pytest
from db.base_class import Base
from db.deps import get_ro_session, get_session
from main import app
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import Session, sessionmaker
from starlette.testclient import TestClient

from tests.api import TEST_API_TOKEN


@pytest.fixture
def temp_session() -> Session:
    SQLALCHEMY_DATABASE_URL = "sqlite://"
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    return TestingSessionLocal()


@pytest.fixture
def authed_client(temp_session: Session) -> TestClient:
    def override_get_session() -> Generator:
        try:
            yield temp_session
        finally:
            temp_session.close()

    app.dependency_overrides[get_session] = override_get_session
    app.dependency_overrides[get_ro_session] = override_get_session

    return TestClient(app, headers={"Authorization": TEST_API_TOKEN})
