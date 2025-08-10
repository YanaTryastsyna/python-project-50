from gendiff.file_reader import read_file
from gendiff.differ import build_diff
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json



def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)
    diff = build_diff(data1, data2)

    if format_name == 'stylish':
        return format_stylish(diff)
    elif format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'json':
        return format_json(diff)
    else:
        raise ValueError(f"Unknown format: {format_name}")
    









        


     




