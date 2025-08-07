from gendiff import generate_diff

def test_diff_nested_json():
    file1 = 'tests/test_data/file_nested1.json'
    file2 = 'tests/test_data/file_nested2.json'
    with open('tests/test_data/expected_stylish.txt') as f:
        expected = f.read()
    assert generate_diff(file1, file2).strip()  == expected.strip() 

