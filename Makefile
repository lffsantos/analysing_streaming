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
	@echo "make build_code_test:"
	@echo "       Generate a build test image"
	@echo ""
	@echo "make run_postgres:"
	@echo "       Run Postgres database"
	@echo ""
	@echo "make test:"
	@echo "       Run tests with coverage, lint, and clean commands"
	@echo ""
	@echo "make development:"
	@echo "       Run app in development mode"
	@echo ""
	@echo "make run:"
	@echo "       Run App in background mode"
	@echo ""
	@echo "make stop:"
	@echo "       Stop Application"
	@echo ""
	@echo "make stop_all:"
	@echo "       Stop Application and Postgres"
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
	sh -c "isort --skip-glob=.tox --recursive . "


copy_env:
	-cp -n .env-example .env

build_code:
	$(DOCKER_COMPOSE) build

run:
	$(DOCKER_COMPOSE) up
