DOCKER_COMPOSE=docker compose
DOCKER_EXEC=$(DOCKER_COMPOSE) exec flask

docker-build:
	$(DOCKER_COMPOSE) up --build -d

docker-stop:
	$(DOCKER_COMPOSE) down

docker-exec:
	$(DOCKER_EXEC) /bin/sh

build-develop:
	FLASK_ENV=development FLASK_DEBUG=1 $(DOCKER_COMPOSE) up --build -d

run-test:
	$(DOCKER_EXEC) pytest

run-linter:
	$(DOCKER_EXEC) flake8