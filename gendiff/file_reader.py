import json
import yaml
import os

def read_file(path):
    _, ext = os.path.splitext(path)
    with open(path) as f:
        if ext == '.json':
            return json.load(f)
        elif ext in ('.yml', '.yaml'):
            return yaml.safe_load(f)
        else:
            raise ValueError(f'Unsupported file format: {ext}')



