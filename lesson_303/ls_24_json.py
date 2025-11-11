import json
from pathlib import Path

file_path = Path(__file__).parent / "file_01.json"

with file_path.open(encoding="utf8") as file:
    try:
        data = json.load(file)
    except json.decoder.JSONDecodeError as e:
        print(e)
        data = None

print(data)
print('status', data.get('status'))

new_data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

new_file_path = Path(__file__).parent / "file_new.json"

with new_file_path.open("w",encoding="utf8") as file:
    json.dump(data, file, indent=2)

json_string = '{"name": "John", "age": 30, "city": "New York"}'
# Розбір JSON-рядка
data = json.loads(json_string)

# Виведення розібраних даних
print(data)

