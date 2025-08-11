import os
from gendiff import generate_diff


def test_plain_format():
    base_dir = os.path.dirname(__file__)
    file1 = os.path.join(base_dir, 'test_data', 'file_nested1.yml')
    file2 = os.path.join(base_dir, 'test_data', 'file_nested2.yml')
    expected_path = os.path.join(base_dir, 'test_data', 'expected_plain.txt')

    with open(expected_path) as f:
        expected = f.read()

    result = generate_diff(file1, file2, format_name='plain')
    assert result.strip() == expected.strip()
