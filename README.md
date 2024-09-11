# Проект personal_data (тестовое задание)

Это маленькое RESTful API приложение написанное на Python, которое 
предоставляет сохранение персональных в виде `ключ: значения = "899999999999":"ул. N, д.N, кв.N"`.
Сохранение идёт в Redis.

## Что нужно сделать перед запуском

Прежде чем запускать данный проект нужно создать файл конфигурации, где есть следующие параметры:
- `REDIS_MAIN_DSN` - DNS для подключения к Redis
- `TITLE_APP` - Название Backend приложения
- `PORT` - Порт для запуска Backend приложения
- `HOST` - Хост для запуска Backend приложения
- `LOGGING_LEVEL` - Уровень логирования, можно указать следующие уровни \["DEBUG", "INFO"]

Имена файла конфигурации могут быть следующие: `.dev_env`, `.test_env`, `.prod_env`. 
Также пример рабочей конфигурации есть в корне проекта `.example_env`.

## Запуск проекта

- Запуск через Docker:
  - ``make full_build_backend``;
- Запуск локально:
  - ``poetry install``;
  - Далее вам нужно подключиться к Redis на вашем компьютере или к удаленному;
  - ``make start_backend_on_gunicorn``;


## Использование

В документации FastAPI сказано, чтобы получить доступ к документации через Swagger вам требуется обратиться 
по следующему пути `http://0.0.0.0:5000/docs`


## Решение второго задания:
При решении данной задачи я использовал PostgreSQL 14.3 с базовой конфигурацией

**Вариант 1**
```sql
with temp_query as (
    select
        fn.name,
        sn.status
    from short_names sn
    join full_names fn on sn.name = split_part(fn.name, '.', 1)::text
)
update full_names
set status = temp_query.status
from temp_query
where temp_query.name = full_names.name;
```
**Вариант 2**
```sql
begin;
with negative_status as (
    select name
    from short_names
    where status = 0
)
update full_names set status = 0
from negative_status ns
where ns.name = split_part(full_names.name, '.', 1)::text;

with positive_status as (
    select name
    from short_names
    where status = 1
)
update full_names set status = 1
from positive_status ps
where ps.name = split_part(full_names.name, '.', 1)::text;
commit;
```