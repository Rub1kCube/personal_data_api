from redis import asyncio as aioredis

from config.settings import get_settings


async def get_personal_data(
        phone_number: str
) -> str | None:

    async with aioredis.Redis(decode_responses=True).from_url(str(get_settings().redis_main_dsn)) as client:
        result = await client.get(phone_number)

    return result


async def create_personal_data(
        phone_number: str,
        address: str,
) -> bool:

    async with aioredis.Redis(decode_responses=True).from_url(str(get_settings().redis_main_dsn)) as client:
        result = await client.set(phone_number, address)

    return result


async def update_personal_data(
        phone_number: str,
        address: str,
) -> bool:

    async with aioredis.Redis(decode_responses=True).from_url(str(get_settings().redis_main_dsn)) as client:
        result = await client.set(phone_number, address)

    return result
