import os
from gendiff import generate_diff


def test_nested_diff():
    base_dir = os.path.dirname(__file__)
    file1 = os.path.join(base_dir, 'test_data', 'file_nested1.json')
    file2 = os.path.join(base_dir, 'test_data', 'file_nested2.json')
    expected_path = os.path.join(base_dir, 'test_data', 'expected_stylish.txt')

    with open(expected_path) as f:
        expected = f.read()

    result = generate_diff(file1, file2)
    assert result.strip() == expected.strip()

