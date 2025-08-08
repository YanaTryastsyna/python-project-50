def format_value(value, depth):
    if isinstance(value, dict): # Если значение — это словарь, нужно отформатировать его как блок с отступами.
        lines = [] #Создаём список строк, который будет содержать все пары "ключ: значение" внутри этого словаря.
        indent = ' ' * (depth * 4) #Вычисляем отступ для текущего уровня глубины. Каждый уровень = 4 пробела, т.е. depth=2 → ' '.
        
        for key, val in value.items():
            lines.append(f"{indent}    {key}: {format_value(val, depth + 1)}") # Добавляем строку " ключ: значение" с нужным отступом. Также вызываем format_value рекурсивно, если val — это снова словарь.
        result = '\n'.join(lines) # Склеиваем все строки с новой строки между ними.
        return f'{{\n{result}\n{indent}}}' #Возвращаем результат как многострочный блок словаря с {}.
    
    elif value is None:
        return 'null'
    
    elif isinstance(value, bool):
        return str(value).lower()
    
    else:
        return str(value)
    
def format_stylish(diff, depth=1):
    lines = []
    base_indent = ' ' * (depth * 4 - 2)  # Для знака +/-
    normal_indent = ' ' * (depth * 4)    # Для обычных строк
    closing_indent = ' ' * ((depth - 1) * 4)

    for item in diff:
        key = item['key']
        status = item['status']

        if status == 'nested':
            children = format_stylish(item['children'], depth + 1)
            lines.append(f'{normal_indent}{key}: {children}')

        elif status == 'added':
            value = format_value(item['value'], depth)
            lines.append(f'{base_indent}+ {key}: {value}')

        elif status == 'removed':
            value = format_value(item['value'], depth)
            lines.append(f'{base_indent}- {key}: {value}')

        elif status == 'unchanged':
            value = format_value(item['value'], depth)
            lines.append(f'{normal_indent}{key}: {value}')

        elif status == 'changed':
            value1 = format_value(item['value1'], depth)
            value2 = format_value(item['value2'], depth)
            lines.append(f'{base_indent}- {key}: {value1}')
            lines.append(f'{base_indent}+ {key}: {value2}')

    return f"{{\n" + "\n".join(lines) + f"\n{closing_indent}}}"

    




  