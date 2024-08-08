import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_return_content(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Head of app' in rv.data
