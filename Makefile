install:
	uv sync

run:
	uv run gendiff

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml

lint:
	uv run ruff check gendiff

check: test lint

build:
	uv build

package-install:
	uv tool install dist/*.whl

reinstall:
	uv tool install --force dist/*.whl

uninstall:
	uv tool uninstall hexlet-code

.PHONY: install test lint selfcheck check build package-install reinstall uninstall