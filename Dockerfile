FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VIRTUALENVS_CREATE=False \
    POETRY_VERSION=1.8.3 \
    PIP_NO_CACHE_DIR=off \
    PYTHONUNBUFFERED=1

# install poetry
RUN pip install poetry==$POETRY_VERSION

# install dependent
COPY poetry.lock pyproject.toml /
RUN poetry install

COPY app /app
COPY .example_env /

EXPOSE 5000
ENTRYPOINT ["poetry", "run", "gunicorn", "-c", "gunicorn.conf.py", "main:configuration_app()"]