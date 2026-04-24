import os

import requests
from faker import Faker


params = {'API_KEY': os.getenv('API_KEY')}
def test_delete_fake_user():
    fake = Faker()
    fake_username = fake.user_name()

    response = requests.delete(f'{os.getenv('DOMAIN_URL')}/users/{fake_username}', params=params, verify=False)

    assert response.status_code == 404, f"Actual response code - {response.status_code}. Text - {response.text}"