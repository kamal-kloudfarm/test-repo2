.ONESHELL:

.PHONY: help
help:		## Show this help message.
	@echo "Usage: make <target>"
	@echo "\nTargets:"
	@fgrep "##" Makefile | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##/ -/'

.PHONY: requirements
requirements:	## Generate the requirements.txt and requirements-dev.txt files.
	poetry export -o requirements.txt --without-hashes
	poetry export -o requirements-dev.txt --with=dev --without-hashes

.PHONY: db-migrate
db-migrate:	## Run the database migrations.
	poetry run python manage.py migrate

.PHONY: db-upgrade
db-upgrade:	## Upgrade the database.
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate

.PHONY: db-flush
db-flush:	## Flush the database.
	poetry run python manage.py flush

.PHONY: run
run:		## Run the development server.
	poetry run python manage.py runserver

.PHONY: shell
shell:		## Run the Django shell.
	poetry run python manage.py shell_plus

.PHONY: injectenv
injectenv:	## Inject the project environment variables to heroku.
	EDITOR='./injectenv' poetry run heroku config:edit