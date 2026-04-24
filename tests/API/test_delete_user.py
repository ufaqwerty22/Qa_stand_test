import os

import pytest
from aiohttp import ClientSession


params = {'API_KEY': os.getenv('API_KEY')}
async def test_delete_user(create_and_delete_user):
    session = ClientSession()
    username = create_and_delete_user

    response = await session.delete(f'{os.getenv('DOMAIN_URL')}/users/{username}', params=params, ssl=False)

    assert response.status == 200, f"Actual response code - {response.status}. Text - {response.text}"
    await session.close()