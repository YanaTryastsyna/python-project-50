from gendiff import generate_diff

def test_flat_diff():
    file1 = 'tests/test_data/file1.json'
    file2 = 'tests/test_data/file2.json'

    with open('tests/test_data/expected_diff.txt') as f:
        expected = f.read()

    result = generate_diff(file1, file2)
    assert result.strip() == expected.strip()    