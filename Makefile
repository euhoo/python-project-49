install:
	poetry install
brain-games:
	poetry run brain-games
bg:
	poetry run brain-games
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
lint: 
	poetry run flake8 brain_games
full:
	make lint; make build; make publish; make package-install