from fastapi import FastAPI

from routers import all_routers
from config.settings import get_settings
from config.logger import logger
from service.connector.connect_redis import check_connect_redis


def configuration_app() -> FastAPI:

    settings = get_settings()

    app = FastAPI(
        title=settings.title_app,
    )
    app.include_router(all_routers)

    if check_connect_redis():
        logger.info("Redis connect")
    else:
        raise SystemExit("Redis not connect")

    logger.info("Backend app end configuration")

    return app
