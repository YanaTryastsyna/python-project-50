lint:
	ruff check .

diff:
	python3 -m gendiff.scripts.gendiff tests/test_data/file1.json tests/test_data/file2.json