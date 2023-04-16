from fastapi.testclient import TestClient
from server import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_history():
    response = client.get("/istoriya/")
    assert response.status_code == 200
    assert response.json() == {"message": "There is no any requests yet"}


def test_predict_positive():
    response = client.post("/predict/",
                           json={"text": "I like machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'POSITIVE'


def test_predict_negative():
    response = client.post("/predict/",
                           json={"text": "I hate machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'NEGATIVE'


def test_history_1():
    response = client.get("/istoriya/")
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['last_answer']['label'] == 'NEGATIVE'