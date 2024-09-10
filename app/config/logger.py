import logging

from config.settings import get_settings


logger = logging.getLogger(get_settings().title_app)
handler = logging.StreamHandler()

formatter = logging.Formatter(
    "[%(levelname)s][%(asctime)s] - %(name)s:%(module)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
handler.setFormatter(formatter)

logger.addHandler(handler)


if get_settings().logging_level == "INFO":
    logger.setLevel(logging.INFO)
else:
    logger.setLevel(logging.DEBUG)
