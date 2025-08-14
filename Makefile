
lint:
	$(PYTHON) -m ruff check .
diff:
	$(PYTHON) -m gendiff.scripts.gendiff tests/test_data/file1.json tests/test_data/file2.json

install:
	uv sync

test:
	python -m pytest -v

test-coverage:
	$(PYTHON) -m pytest --cov=gendiff --cov-report=xml:coverage.xml

check: lint  # Упрощаем вызов

.PHONY: install test lint check test-coverage diff