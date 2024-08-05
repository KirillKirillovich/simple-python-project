import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_return_content(client):
    rv = client.get('/')
    assert rv.status_code == 200
