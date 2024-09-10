from redis import Redis
from config.settings import get_settings


def check_connect_redis() -> bool:
    with Redis(decode_responses=True).from_url(str(get_settings().redis_main_dsn)) as client:
        response = client.ping()
        return response
