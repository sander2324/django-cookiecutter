default: clean install migrate

clean:
	find . -name '*.pyc' -exec rm -rf {} +
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*.egg-info' -exec rm -rf {} +

install:
	pip3 install -r requirements.txt
	pip3 install -e .

install-prod:
	pip3 install -r requirements/production.txt
	pip3 install -e .

migrate:
	manage.py migrate

lint:
	flake8 src
	black --check --diff src
	isort --check-only --diff src

format:
	black src
	isort src

makemessages:
	cd src/{{cookiecutter.project_slug}} && manage.py makemessages --no-location --all

compilemessages:
	cd src/{{cookiecutter.project_slug}} && manage.py compilemessages
