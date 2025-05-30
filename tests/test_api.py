from app import create_app
import pytest
import json


def load_test_data(path = "tests/receipts.json"):
    with open(path, 'r') as file:
        data = json.load(file)
    return [(entry['receipt'], entry['expected_points']) for entry in data]


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
        

@pytest.mark.parametrize("receipt,expected_points", load_test_data())
def test_receipt_process(client, receipt, expected_points):
    
    # call process endpoint and get an id
    res = client.post('/receipts/process', json=receipt)
    assert res.status_code == 200
    data = res.get_json()
    assert 'id' in data
    id = data['id']

    # call points endpoint with the id
    res = client.get(f'/receipts/{id}/points')
    assert res.status_code == 200
    data = res.get_json()
    assert 'points' in data
    points = data['points']
    assert points == expected_points


def test_invalid_receipt_id(client):
    id = "c6a6b488-124f-4c4e-9b6a-0273e0443b46"
    res = client.get(f'/receipts/{id}/points')
    assert res.status_code == 404
