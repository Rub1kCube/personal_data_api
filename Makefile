start_backend_on_gunicorn:
	poetry run gunicorn -c ./app/gunicorn.conf.py "main:configuration_app()"


full_build_backend:
	docker-compose -f docker-compose.yml up --detach --build


stop_backend:
	docker-compose -f docker-compose.yml stop