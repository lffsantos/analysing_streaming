DOCKER_COMPOSE=docker-compose
DOCKER_COMPOSE_TEST=docker-compose -f docker-compose_testing.yml

GIT_CURRENT_BRANCH := ${shell git symbolic-ref --short HEAD}

.PHONY: help clean test clean-build isort run

.DEFAULT: help

help:
	@echo "make clean:"
	@echo "       Removes all pyc, pyo and __pycache__"
	@echo ""
	@echo "make clean-build:"
	@echo "       Clear all build directories"
	@echo ""
	@echo "make isort:"
	@echo "       Run isort command cli in development features"
	@echo ""
	@echo "make copy_env"
	@echo "       Creates .env file base on .env-example"
	@echo ""
	@echo "make build_code:"
	@echo "       Generate a build image"
	@echo ""
	@echo "make test:"
	@echo "       Run tests with coverage, lint, and clean commands"
	@echo ""
	@echo "make run_all_services:"
	@echo "       Run all services in background mode"
	@echo ""
	@echo "make test:"
	@echo "       run testes"
	@echo ""
	@echo "make black:"
	@echo "       run black
	@echo ""
	@echo ""
	@echo "make lint:"
	@echo "       run lint
	@echo ""

clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . | grep -E "__pycache__|.pytest_cache|.pyc|.DS_Store$$" | xargs rm -rf

clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

isort:
	sh -c "isort --skip-glob=.tox . "

copy_env:
	-cp -n .env-example .env

build_code:
	$(DOCKER_COMPOSE) build

run_all_services:
	$(DOCKER_COMPOSE) up -d

elasticsearch:
	$(DOCKER_COMPOSE) up -d es01

kibana:
	$(DOCKER_COMPOSE) up -d elasticsearch kibana

## Lint your code using pylint
.PHONY: lint
lint:
	python -m pylint analysingstream

.PHONY: test
test:
	python -m pytest --version
	python -m pytest tests## Format your code using black
.PHONY: black
black:
	python -m black .
