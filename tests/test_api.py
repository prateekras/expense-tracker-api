from datetime import date
from decimal import Decimal

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base, get_db
from app.main import app


@pytest.fixture()
def client():
    test_engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)
    Base.metadata.create_all(bind=test_engine)

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=test_engine)


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_create_and_get_expense(client):
    payload = {
        "title": "Coffee",
        "amount": "120.50",
        "category": "Food",
        "description": "Coffee with a friend",
        "spent_on": str(date.today()),
    }
    created = client.post("/expenses", json=payload)
    assert created.status_code == 201
    assert created.json()["title"] == "Coffee"

    expense_id = created.json()["id"]
    fetched = client.get(f"/expenses/{expense_id}")
    assert fetched.status_code == 200
    assert Decimal(fetched.json()["amount"]) == Decimal("120.50")


def test_update_and_delete_expense(client):
    created = client.post(
        "/expenses",
        json={"title": "Bus", "amount": "30.00", "category": "Travel"},
    )
    expense_id = created.json()["id"]

    updated = client.patch(f"/expenses/{expense_id}", json={"amount": "45.00"})
    assert updated.status_code == 200
    assert Decimal(updated.json()["amount"]) == Decimal("45.00")

    deleted = client.delete(f"/expenses/{expense_id}")
    assert deleted.status_code == 204
    assert client.get(f"/expenses/{expense_id}").status_code == 404
