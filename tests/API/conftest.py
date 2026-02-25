import os
import uuid

import pytest
import requests


@pytest.fixture
def create_and_delete_user():
    name = f'user_{str(uuid.uuid4())[:6]}'
    password = f'pass_{str(uuid.uuid4())[:6]}'
    params = {'API_KEY': os.getenv('API_KEY')}

    payload = {
        "admin": False,
        "age": 41,
        "description": "Лучший тестер в мире",
        "jobtitle": "Тестировщик",
        "name": "Автоматизатор Тестович",
        "password": password,
        "username": name
    }

    response = requests.post(f'{os.getenv('DOMAIN_URL')}/users', json=payload, params=params)

    yield name

    resp_for_delete_user = requests.get(f'{os.getenv('DOMAIN_URL')}/users/{payload.get('username')}', params=params)
    user_for_delete_json = resp_for_delete_user.json()

    if user_for_delete_json.get('username') == payload.get('username'):
        delete_user = requests.delete(f'{os.getenv('DOMAIN_URL')}/users/{name}')