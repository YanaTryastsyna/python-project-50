from gendiff import generate_diff

def test_flat_diff_yaml():
    file1 = 'tests/test_data/file1.yml'
    file2 = 'tests/test_data/file2.yml'

    expected = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

    result = generate_diff(file1, file2)
    assert result.strip() == expected.strip()

