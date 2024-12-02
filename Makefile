export COMPOSE_DOCKER_CLI_BUILD=1
export DOCKER_BUILDKIT=1
export COMPOSE_IGNORE_ORPHANS=1

bi:
	black . && isort .
build:
	docker compose -f app.yml -f postgres.yml build
up: build
	docker compose -f app.yml -f postgres.yml up -d
up-postgres:
	docker compose -f postgres.yml up -d
up-pgadmin:
	docker compose -f pgadmin.yml up -d --no-recreate
up-all: build up-postgres up-pgadmin
	docker compose -f app.yml -f postgres.yml up -d
unit: up
	docker compose -f app.yml -f postgres.yml run --rm --entrypoint="pytest tests/unit" images-app
down:
	docker compose -f app.yml -f postgres.yml down
down-all:
	docker compose -f postgres.yml down --remove-orphans
logs:
	docker compose -f app.yml -f postgres.yml logs --tail=25 images-app
sh:
	docker exec -it images-app bash
migrate:
	docker exec -it images-app python manage.py migrate
migrations:
	docker exec -it images-app python manage.py makemigrations
superuser:
	docker exec -it images-app python manage.py createsuperuser