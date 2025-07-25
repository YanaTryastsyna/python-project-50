
from hexlet_code.file_reader import read_file

def generate_diff(file_path1, file_path2):
    # Читаем и парсим два файла
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)

    # Собираем все ключи (объединение множеств)
    keys = sorted(set(data1.keys()) | set(data2.keys()))

    result = ["{"]  # начинаем формировать строку результата

    for key in keys:
        if key in data1 and key not in data2:
            result.append(f"  - {key}: {data1[key]}")
        elif key not in data1 and key in data2:
            result.append(f"  + {key}: {data2[key]}")
        elif data1[key] != data2[key]:
            result.append(f"  - {key}: {data1[key]}")
            result.append(f"  + {key}: {data2[key]}")
        else:
            result.append(f"    {key}: {data1[key]}")

    result.append("}")
    return "\n".join(result)
    






        


     




