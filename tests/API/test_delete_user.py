import os

import requests
from faker import Faker


params = {'API_KEY': os.getenv('API_KEY')}
def test_delete_user(create_and_delete_user):
    username = create_and_delete_user

    response = requests.delete(f'{os.getenv('DOMAIN_URL')}/users/{username}', params=params, verify=False)

    assert response.status_code == 200, f"Actual response code - {response.status_code}. Text - {response.text}"