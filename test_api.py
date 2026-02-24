import os

import requests
from dotenv import load_dotenv
load_dotenv()


params = {'API_KEY': os.getenv('API_KEY')}
def test_delete_user(create_and_delete_user):
    username = create_and_delete_user

    response = requests.delete(f'{os.getenv('DOMAIN_URL')}/users/{username}', params=params)

    assert response.status_code == 200, f"Actual response code - {response.status_code}. Text - {response.text}"


def test_update_user(create_and_delete_user):
    username = create_and_delete_user

    update_payload = {
        'username': 'MilkaMaker',
        'age': 17
    }

    response = requests.put(f'{os.getenv('DOMAIN_URL')}/users/{username}', json=update_payload, params=params)

    assert response.status_code == 200, f"Actual response code - {response.status_code}. Text - {response.text}"


def test_delete_fake_user(create_and_delete_user):
    fake_username = 'l;asldkopq'

    response = requests.delete(f'{os.getenv('DOMAIN_URL')}/users/{fake_username}', params=params)

    assert response.status_code == 404, f"Actual response code - {response.status_code}. Text - {response.text}"