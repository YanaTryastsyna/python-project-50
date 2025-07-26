import json

def read_file(path):
    with open(path) as f:
        return json.load(f)
    

   