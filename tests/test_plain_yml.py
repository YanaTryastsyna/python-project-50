from gendiff import generate_diff

def test_plain_format():
    file1 = 'tests/test_data/file_nested1.yml'
    file2 = 'tests/test_data/file_nested2.yml'

    with open('tests/test_data/expected_plain.txt') as f:
        expected = f.read()

    result = generate_diff(file1, file2, format_name='plain')
    assert result.strip() == expected.strip()