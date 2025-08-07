def build_diff(data1, data2):
    keys = sorted(set(data1.keys()) | set(data2.keys())) #объединяет множества ключей (все уникальные ключи из обоих словарей)
    diff = []

    for key in keys:
        if key not in data2:
            diff.append({
                'key': key,
                'status': 'removed',
                'value': data1[key]
            })

        elif key not in data1:
            diff.append({
                'key': key,
                'status': 'added',
                'value': data2[key]
            })

        elif isinstance(data1[key], dict) and isinstance(data2[key], dict): #Если в обоих файлах под этим ключом находятся вложенные словари — это означает, что структура вложенная, и нужно сравнивать их рекурсивно.
            diff.append({
                'key': key,
                'status': 'nested',
                'children': build_diff(data1[key] , data2[key])
            })
        
        elif data1[key] == data2[key]:
            diff.append({
                'key': key,
                'status': 'unchanged',
                'value': data1[key]
            })
        
        else:
            diff.append({
                'key': key,
                'status': 'changed',
                'value1': data1[key],
                'value2': data2[key]
            })
    return diff



