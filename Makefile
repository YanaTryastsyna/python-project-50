lint:
	uv run ruff check --fix gendiff tests

diff:
	python3 -m gendiff.scripts.gendiff tests/test_data/file1.json tests/test_data/file2.json

install:
	uv sync

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml

check: 
	make lint

.PHONY: install test lint check test-coverage diff