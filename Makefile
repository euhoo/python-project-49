install:
	poetry install
brain-games:
	poetry run brain-games
play-bg:
	poetry run brain-games
play-be:
	poetry run brain-even
play-bc:
	poetry run brain-calc
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
package-install-force:
	python3 -m pip install --force-reinstall --user dist/*.whl
lint: 
	poetry run flake8 brain_games
full:
	make lint; make build; make publish; make package-install-force