# **Gendiff** — сравнение конфигурационных файлов

### CI and Linter Status
[![Build Status](https://github.com/YanaTryastsyna/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/YanaTryastsyna/python-project-50/actions/workflows/hexlet-check.yml)  
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=YanaTryastsyna_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=YanaTryastsyna_python-project-50)  
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=YanaTryastsyna_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=YanaTryastsyna_python-project-50)

---

## 📌 Описание проекта
**Gendiff** — консольная утилита для сравнения двух конфигурационных файлов в форматах **JSON** и **YAML**.  
Подходит для анализа изменений между версиями настроек и интеграции с другими системами.

---

## 🚀 Возможности
- Поддержка **JSON** и **YAML**
- Сравнение как плоских, так и вложенных структур
- Три формата вывода:
  - **Stylish** — древовидный
  - **Plain** — плоский человеко-читаемый
  - **JSON** — машинно-читаемый
- CLI-интерфейс с выбором формата
- Удобные команды в `Makefile`

---

## 🛠 Используемые технологии
- **Python** 3.12+
- **argparse** — разбор аргументов командной строки
- **PyYAML** — парсинг YAML
- **json** — работа с JSON
- **pytest** — модульное тестирование
- **ruff** — линтер и автоформатирование
- **make** — автоматизация команд
- **GitHub Actions** — CI/CD
- **SonarCloud** — анализ качества кода

## 📦 Установка
```bash
git clone https://github.com/YanaTryastsyna/python-project-50.git
cd python-project-50
make install
``` 

## ▶️ Запуск
gendiff file1.json file2.json
gendiff file1.yml file2.yml --format plain
gendiff file1.json file2.json --format json

## 🧪 Тестирование
make test


## Примеры работы
JSON-файлы:
[![asciicast](https://asciinema.org/a/ryBs0phVPHxiW6wbsyCrdN4UU.svg)](https://asciinema.org/a/ryBs0phVPHxiW6wbsyCrdN4UU)

YAML-файлы:
[![asciicast](https://asciinema.org/a/vj0v9h3H8gJJyhsx7scYJX1n9.svg)](https://asciinema.org/a/vj0v9h3H8gJJyhsx7scYJX1n9)

Вложенные структуры:
[![asciicast](https://asciinema.org/a/j3t1f2BGYzhnzYg1QJuOiNG5H.svg)](https://asciinema.org/a/j3t1f2BGYzhnzYg1QJuOiNG5H)

Плоский формат:
[![asciicast](https://asciinema.org/a/FJ7Auy3wyFPzTvxZ3Do6OfcfR.svg)](https://asciinema.org/a/FJ7Auy3wyFPzTvxZ3Do6OfcfR)

Формат JSON:
[![asciicast](https://asciinema.org/a/dwzxH5jw5Ha2VEhEKTBC4r1iO.svg)](https://asciinema.org/a/dwzxH5jw5Ha2VEhEKTBC4r1iO)

## 📂 Структура проекта
gendiff/          # Исходный код
gendiff/formatters # Форматеры (stylish, plain, json)
gendiff/scripts   # CLI
tests/            # Тесты
Makefile          # Автоматизация
pyproject.toml    # Конфигурация проекта
ruff.toml         # Настройки линтера

## 👤 Автор
Яна Трястына
📧 Email: yana.tryastsyna@mail.ru
🔗 GitHub: YanaTryastsyna


