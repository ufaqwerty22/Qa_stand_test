import os
import uuid

import pytest
import requests
from dotenv import load_dotenv
from faker import Faker
load_dotenv()


@pytest.fixture(scope='function')
def create_and_delete_user():
    fake = Faker()
    name = fake.name()
    password = fake.password(length=6)
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

    requests.post(f'{os.getenv('DOMAIN_URL')}/users', json=payload, params=params, verify=False)

    yield name

    user_to_delete_json = requests.get(f'{os.getenv('DOMAIN_URL')}/users/{payload.get('username')}',
                                        params=params, verify=False).json()

    if user_to_delete_json.get('username') == payload.get('username'):
        requests.delete(f'{os.getenv('DOMAIN_URL')}/users/{name}', verify=False)