def format_value(value, depth):
    indent = ' ' * (depth * 4)
    if isinstance(value, dict):
        lines = []
        for k, v in value.items():
            lines.append(f"{indent}    {k}: {format_value(v, depth + 1)}")
        return "{\n" + "\n".join(lines) + f"\n{indent}}}"
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return str(value)


def format_stylish(diff, depth=1):
    lines = []
    indent = ' ' * (depth * 4 - 2)

    for item in diff:
        key = item['key']
        status = item['status']

        if status == 'nested':
            children = format_stylish(item['children'], depth + 1)
            lines.append(f"{' ' * (depth * 4)}{key}: {children}")
        elif status == 'added':
            val = format_value(item['value'], depth)
            lines.append(f"{indent}+ {key}: {val}")
        elif status == 'removed':
            val = format_value(item['value'], depth)
            lines.append(f"{indent}- {key}: {val}")
        elif status == 'unchanged':
            val = format_value(item['value'], depth)
            lines.append(f"{' ' * (depth * 4)}{key}: {val}")
        elif status == 'changed':
            val1 = format_value(item['value1'], depth)
            val2 = format_value(item['value2'], depth)
            lines.append(f"{indent}- {key}: {val1}")
            lines.append(f"{indent}+ {key}: {val2}")

    return "{\n" + "\n".join(lines) + "\n" + (' ' * ((depth - 1) * 4)) + "}"