import pytest
import app
from controllers import food

@pytest.fixture
def api(monkeypatch):
    test_food = [
        {'id': 1, 'name': 'Test Food 1'},
        {'id': 2, 'name': 'Test Food 2'}
    ]
    #second argument inside monkeypatch.setattr needs to match the list inside food.py
    monkeypatch.setattr(food, "foods", test_food)
    api = app.app.test_client()
    return api
