import os
import json
from gendiff import generate_diff

def test_diff_json_format():
    base_dir = os.path.dirname(__file__)
    file1 = os.path.join(base_dir, 'test_data', 'file_nested1.json')
    file2 = os.path.join(base_dir, 'test_data', 'file_nested2.json')

    result = generate_diff(file1, file2, format_name='json')
    parsed = json.loads(result)
    assert isinstance(parsed, list)
    assert all(isinstance(item, dict) for item in parsed)
