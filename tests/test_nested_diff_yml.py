from gendiff import generate_diff

def test_nested_diff_yaml():
    file1 = 'tests/test_data/file_nested1.yml'
    file2 = 'tests/test_data/file_nested2.yml'

    with open('tests/test_data/expected_stylish.txt') as f:
        expected = f.read()

    result = generate_diff(file1, file2)
    assert result.strip() == expected.strip()


    