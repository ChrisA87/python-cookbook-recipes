lint:
	flake8 recipes

test:
	coverage run --source recipes -m pytest tests
