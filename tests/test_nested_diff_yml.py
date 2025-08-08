from gendiff import generate_diff

def test_diff_nested_yml():
    file1 = 'tests/test_data/file_nested1.yml'
    file2 = 'tests/test_data/file_nested2.yml'
    expected_file = 'tests/test_data/expected_stylish.txt'  

    with open(expected_file) as f:
        expected = f.read()

    result = generate_diff(file1, file2, format_name='stylish')
    assert result.strip() == expected.strip()