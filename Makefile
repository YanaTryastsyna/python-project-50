lint:
	python -m ruff check .
diff:
	python -m gendiff.scripts.gendiff tests/test_data/file1.json tests/test_data/file2.json

install:
	uv sync

test:
	python -m pytest -v

test-coverage:
	python -m pytest --cov=gendiff --cov-report=xml:coverage.xml

check: 
	make lint

.PHONY: install test lint check test-coverage diff