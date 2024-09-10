from multiprocessing import cpu_count
from pathlib import Path

from config.settings import get_settings


def max_workers():
    return cpu_count()


settings = get_settings()

bind = settings.url
max_requests = 1000
worker_class = 'uvicorn.workers.UvicornWorker'
workers = 4
reload = True
chdir = str(Path(__file__).absolute().parent)

