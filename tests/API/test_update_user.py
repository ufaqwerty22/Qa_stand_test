import os

from aiohttp import ClientSession


params = {'API_KEY': os.getenv('API_KEY')}
async def test_update_user(create_and_delete_user):
    session = ClientSession()
    username = create_and_delete_user
    update_payload = {
        'username': 'MilkaMaker',
        'age': 17
    }

    response = await session.put(f'{os.getenv('DOMAIN_URL')}/users/{username}',
                            json=update_payload, params=params, ssl=False)

    body = await response.text()
    assert response.status == 200, f"Actual response code - {response.status}. Text - {body}"

    await session.close()
