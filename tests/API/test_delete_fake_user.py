import os

from aiohttp import ClientSession
from faker import Faker

params = {'API_KEY': os.getenv('API_KEY')}
async def test_delete_fake_user():
    session = ClientSession()
    fake = Faker()
    fake_username = fake.user_name()

    response = await session.delete(f'{os.getenv('DOMAIN_URL')}/users/{fake_username}', params=params, ssl=False)

    assert response.status == 404, f"Actual response code - {response.status}. Text - {response.text}"
    await session.close()