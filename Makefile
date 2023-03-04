lint:
	flake8 recipes

test:
	coverage run --source recipes -m pytest tests

pip-install:
	pip install pip-tools
	pip-compile
	pip-sync
