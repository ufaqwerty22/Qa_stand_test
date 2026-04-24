import os

import asyncio
import pytest_asyncio
from aiohttp import ClientSession
from dotenv import load_dotenv
from faker import Faker
load_dotenv()


@pytest_asyncio.fixture(scope='function')
async def create_and_delete_user():
    session = ClientSession()
    fake = Faker('ru_RU')
    username = await asyncio.to_thread(fake.user_name)
    password = await asyncio.to_thread(fake.password)
    params = {'API_KEY': os.getenv('API_KEY')}

    payload = {
        "admin": False,
        "age": 41,
        "description": "Лучший тестер в мире",
        "jobtitle": "Тестировщик",
        "name": "Автоматизатор Тестович",
        "password": password,
        "username": username
    }

    await session.post(f'{os.getenv('DOMAIN_URL')}/users', json=payload, params=params, ssl=False)

    yield username

    user_to_delete = await session.get(f'{os.getenv('DOMAIN_URL')}/users/{payload.get('username')}',
                                        params=params, ssl=False)
    user_to_delete_json = await user_to_delete.json()

    if user_to_delete_json.get('username') == payload.get('username'):
        await session.delete(f'{os.getenv('DOMAIN_URL')}/users/{username}', ssl=False)
    await session.close()