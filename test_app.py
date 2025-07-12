import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to Flask!" in response.data

def test_greet_with_name(client):
    response = client.get('/greet?name=Rishabh')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, Rishabh!"}

def test_greet_without_name(client):
    response = client.get('/greet')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, Guest!"}
