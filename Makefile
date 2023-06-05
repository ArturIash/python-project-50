install:
	poetry install

build:
	poetry build

gendiff:
	poetry run gendiff -h

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl --force-reinstall

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -vv

test-cov:
	poetry run pytest --cov=gendiff --cov-report xml
