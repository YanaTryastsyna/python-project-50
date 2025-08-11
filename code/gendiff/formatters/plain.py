def to_str(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return str(value)

def format_plain(diff, path=""):
    lines = []
    for item in diff:
        key = item['key']
        property_path = f"{path}{key}"
        status = item['status']

        if status == 'nested':
            lines.append(format_plain(item['children'], f"{property_path}."))
        elif status == 'added':
            value = to_str(item['value'])
            lines.append(
                f"Property '{property_path}' was added with value: {value}"
            )
        elif status == 'removed':
            lines.append(f"Property '{property_path}' was removed")
        elif status == 'changed':
            value1 = to_str(item['value1'])
            value2 = to_str(item['value2'])
            lines.append(
                f"Property '{property_path}' was updated. "
                f"From {value1} to {value2}"
            )
    return "\n".join(lines)


